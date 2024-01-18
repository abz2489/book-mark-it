from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Book(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=125)
    summary = models.TextField(max_length=255)
    author = models.CharField(max_length=125)
    published = models.DateField(null=True, blank=True)
    isbn = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cover_url = models.URLField(max_length=1024, null=True, blank=True)
    cover = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
    