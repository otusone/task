from django.contrib import admin
from .models import Product, Varients

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','class_name','image', 'status']


@admin.register(Varients)
class VarientsAdmin(admin.ModelAdmin):
    list_display = ['id','product_name','title','availableStock']