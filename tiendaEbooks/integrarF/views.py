from django.shortcuts import render, get_object_or_404
from .models import Ebook
from django.http import FileResponse

# Página principal
def home(request):
    featured_ebooks = Ebook.objects.all()[:6]  # 6 destacados
    return render(request, "integrarF/home.html", {"ebooks": featured_ebooks})

# Página por categoría
def category(request, category_name):
    ebooks = Ebook.objects.filter(category=category_name)
    return render(request, "integrarF/category.html", {"ebooks": ebooks, "category": category_name})

# Página individual
def ebook_detail(request, ebook_id):
    ebook = get_object_or_404(Ebook, id=ebook_id)
    return render(request, "integrarF/detail.html", {"ebook": ebook})

# Descarga
def download_file(request, ebook_id):
    ebook = get_object_or_404(Ebook, id=ebook_id)
    ebook.download_count += 1
    ebook.save()
    return FileResponse(
        ebook.file.open("rb"),
        as_attachment=True,
        filename=ebook.title + "." + ebook.file.name.split(".")[-1]
    )
