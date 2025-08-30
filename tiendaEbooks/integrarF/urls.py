from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("categoria/<str:category_name>/", views.category, name="category"),
    path("ebook/<int:ebook_id>/", views.ebook_detail, name="ebook_detail"),
    path("ebook/<int:ebook_id>/download/", views.download_file, name="download_file"),
]
