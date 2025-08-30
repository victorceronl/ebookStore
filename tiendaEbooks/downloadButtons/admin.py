from django.contrib import admin
from .models import File, Download

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ("name", "file", "download_count")

@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    list_display = ("file", "downloaded_at")
