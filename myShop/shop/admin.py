from django.contrib import admin
from .models import *


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'stock', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'stock']
    list_editable = ['price', 'stock', 'available']


admin.site.register(Product, ProductAdmin)
