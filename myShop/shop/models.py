from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)


class Product(models.Model):
    category = models.ManyToManyField('Category', related_name='products')
    name = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='img/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default=0)
