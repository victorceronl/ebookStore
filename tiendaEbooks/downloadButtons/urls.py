from django.urls import path
from . import views

urlpatterns = [
    path("", views.file_list, name="file_list"),  
    path("download/<int:file_id>/", views.download_file, name="download_file"),
]
