from django.db import models

CATEGORY_CHOICES = [
    ('Negocios', 'Negocios'),
    ('BestSellers', 'BestSellers'),
    ('Otros', 'Otros'),
]

class Ebook(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    cover = models.ImageField(upload_to="covers/", blank=True, null=True)
    file = models.FileField(upload_to="ebooks/")
    sample_file = models.FileField(upload_to="samples/", blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    publication_date = models.DateField()
    pages = models.PositiveIntegerField(default=0)
    download_count = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Otros')

    def __str__(self):
        return self.title
