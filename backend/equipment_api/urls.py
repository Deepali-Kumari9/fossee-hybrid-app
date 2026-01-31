from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_csv),
    path('summary/', views.equipment_summary),
    path('datasets/', views.dataset_history),
    path('equipment/', views.equipment_list),  
    path("download-report/", views.download_pdf_report),
    path('login/', views.login_user),
]
