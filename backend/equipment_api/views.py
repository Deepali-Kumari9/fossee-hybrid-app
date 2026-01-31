from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.http import JsonResponse, FileResponse
from django.db.models import Avg, Count

from .models import Equipment, Dataset
import pandas as pd

from .reports.pdf_generator import generate_pdf

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


# =========================
# STEP 1: EQUIPMENT LIST (OPEN)
# =========================
@api_view(['GET'])
def equipment_list(request):
    equipment = Equipment.objects.all()

    data = []
    for item in equipment:
        data.append({
            "name": item.name,
            "type": item.type,
            "temperature": item.temperature,
            "pressure": item.pressure,
            "flowrate": item.flowrate
        })

    return Response(data)


# =========================
# STEP 2: CSV UPLOAD (PROTECTED)
# =========================
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_csv(request):
    file = request.FILES.get('file')

    if not file:
        return Response({"error": "No file uploaded"}, status=400)

    df = pd.read_csv(file)
    dataset = Dataset.objects.create(name=file.name)

    for _, row in df.iterrows():
        Equipment.objects.create(
            dataset=dataset,
            name=str(row.get('Equipment Name', 'Unknown')),
            type=str(row.get('Type', 'Unknown')),
            flowrate=float(row.get('Flowrate', 0)),
            pressure=float(row.get('Pressure', 0)),
            temperature=float(row.get('Temperature', 0)),
        )

    return Response({
        "status": "success",
        "message": "CSV uploaded successfully 🚀"
    })


# =========================
# STEP 3: SUMMARY API (PROTECTED)
# =========================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def equipment_summary(request):
    total_equipment = Equipment.objects.count()

    averages = Equipment.objects.aggregate(
        avg_flowrate=Avg('flowrate'),
        avg_pressure=Avg('pressure'),
        avg_temperature=Avg('temperature')
    )

    type_distribution = (
        Equipment.objects
        .values('type')
        .annotate(count=Count('type'))
    )

    return Response({
        "total_equipment": total_equipment,
        "average_flowrate": round(averages['avg_flowrate'], 2) if averages['avg_flowrate'] else 0,
        "average_pressure": round(averages['avg_pressure'], 2) if averages['avg_pressure'] else 0,
        "average_temperature": round(averages['avg_temperature'], 2) if averages['avg_temperature'] else 0,
        "type_distribution": {
            item['type']: item['count'] for item in type_distribution
        }
    })


# =========================
# STEP 4: DATASET HISTORY (OPEN)
# =========================
def dataset_history(request):
    datasets = Dataset.objects.order_by('-uploaded_at')[:5]

    return JsonResponse({
        "datasets": [
            {
                "id": d.id,
                "name": d.name,
                "uploaded_at": d.uploaded_at,
                "equipment_count": d.equipments.count()
            }
            for d in datasets
        ]
    })


# =========================
# STEP 5: PDF REPORT (PROTECTED)
# =========================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def download_pdf_report(request):
    total_equipment = Equipment.objects.count()

    averages = Equipment.objects.aggregate(
        avg_flowrate=Avg('flowrate'),
        avg_pressure=Avg('pressure'),
        avg_temperature=Avg('temperature')
    )

    summary = {
        "total_equipment": total_equipment,
        "average_flowrate": round(averages['avg_flowrate'], 2) if averages['avg_flowrate'] else 0,
        "average_pressure": round(averages['avg_pressure'], 2) if averages['avg_pressure'] else 0,
        "average_temperature": round(averages['avg_temperature'], 2) if averages['avg_temperature'] else 0,
    }

    equipment = Equipment.objects.values(
        "name", "type", "temperature", "pressure", "flowrate"
    )

    pdf_path = generate_pdf(summary, list(equipment))

    return FileResponse(
        open(pdf_path, "rb"),
        as_attachment=True,
        filename="Chemical_Equipment_Report.pdf"
    )


# =========================
# STEP 6: LOGIN API (OPEN)
# =========================
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({"error": "Invalid username"}, status=400)

    if not user.check_password(password):
        return Response({"error": "Invalid password"}, status=400)

    token, _ = Token.objects.get_or_create(user=user)

    return Response({
        "token": token.key,
        "message": "Login successful"
    })
