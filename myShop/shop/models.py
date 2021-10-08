from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200, unique=True, default='')

    class Meta:
        ordering = ('name',)  # Сортировка
        verbose_name_plural = 'Categories'  # Множественное число

    def __str__(self):  # Строковое представление экземпляра модели
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', related_name='product', on_delete=models.CASCADE,
                                 blank=True)  # Продукт не может существовать без категория, поэтому CASCADE
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='img/')
    price = models.DecimalField(max_digits=10, decimal_places=2) # Фиксированная точность, 10 цифр, 2 знака посе запятой
    available = models.BooleanField(default=True) # Доступен ли товар
    stock = models.PositiveIntegerField(default=0) # Количество товара на складе
    slug = models.SlugField(max_length=200, unique=True, default='') # Более корректный "человеческий" url адрес

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self):
        return self.name
