from django.urls import path
from . import views

urlpatterns = [
    path('', views.UploadFileView.as_view(), name='upload_file'),
    path('export_to_excel/', views.export_to_excel, name='export_to_excel'),
]
