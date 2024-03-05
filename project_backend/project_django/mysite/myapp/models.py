from django.db import models

# Create your models here.

class Book(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    book_image = models.ImageField(default='default.jpg',upload_to='book_images/')