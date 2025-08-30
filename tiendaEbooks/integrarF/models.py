from django.db import models
from django.utils import timezone

class File(models.Model):
    name = models.CharField(max_length=200, unique=True)   # Nombre del archivo
    file = models.FileField(upload_to="downloads/")        # Guardado en /media/downloads/
    download_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.download_count} descargas)"


class Download(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name="downloads")
    downloaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.file.name} descargado el {self.downloaded_at}"
