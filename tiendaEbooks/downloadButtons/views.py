from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from django.utils import timezone
from .models import File, Download

# Vista para listar todos los archivos
def file_list(request):
    files = File.objects.all()
    return render(request, "downloadButtons/files.html", {"files": files})

# Vista para descargar un archivo específico
def download_file(request, file_id):
    file_obj = get_object_or_404(File, id=file_id)

    # Registrar la descarga
    Download.objects.create(file=file_obj, downloaded_at=timezone.now())

    # Incrementar contador
    file_obj.download_count += 1
    file_obj.save()

    # Retornar archivo al usuario
    return FileResponse(file_obj.file.open("rb"), as_attachment=True, filename=file_obj.file.name)
