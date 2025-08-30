from django.contrib import admin
from .models import Ebook

@admin.register(Ebook)
class EbookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'publication_date', 'download_count')
    list_filter = ('category', 'publication_date')
    search_fields = ('title', 'description')
