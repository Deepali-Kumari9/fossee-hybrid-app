import os
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from django.conf import settings


def generate_pdf(summary, equipment_list):
    # -------- FILE PATH --------
    report_dir = os.path.join(settings.BASE_DIR, "reports")
    os.makedirs(report_dir, exist_ok=True)

    pdf_path = os.path.join(report_dir, "Chemical_Equipment_Report.pdf")

    # -------- DOCUMENT --------
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=landscape(A4),
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30,
    )

    elements = []
    styles = getSampleStyleSheet()

    # -------- TITLE --------
    elements.append(Paragraph("<b>Chemical Equipment Report</b>", styles["Title"]))
    elements.append(Spacer(1, 20))

    # -------- SUMMARY --------
    summary_table = Table([
        ["Total Equipment", summary["total_equipment"]],
        ["Average Flowrate", summary["average_flowrate"]],
        ["Average Pressure", summary["average_pressure"]],
        ["Average Temperature", summary["average_temperature"]],
    ], colWidths=[300, 200])

    summary_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (1, 0), (-1, -1), "CENTER"),
    ]))

    elements.append(summary_table)
    elements.append(Spacer(1, 30))

    # -------- EQUIPMENT TABLE --------
    table_data = [
        ["Name", "Type", "Temperature (°C)", "Pressure (bar)", "Flowrate (m³/hr)"]
    ]

    for eq in equipment_list:
        table_data.append([
            eq["name"],
            eq["type"],
            eq["temperature"],
            eq["pressure"],
            eq["flowrate"],
        ])

    equipment_table = Table(
        table_data,
        colWidths=[180, 140, 160, 160, 160],
        repeatRows=1
    )

    equipment_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (2, 1), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTSIZE", (0, 1), (-1, -1), 9),
    ]))

    elements.append(equipment_table)

    # -------- BUILD PDF --------
    doc.build(elements)

    return pdf_path
