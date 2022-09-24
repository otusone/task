from django.db import models

# Create your models here.

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='name', null=True, blank=True, unique=True)
    price = models.CharField(max_length=100, verbose_name='price', null=True, blank=True)
    class_name = models.CharField(max_length=100, verbose_name='class', null=True, blank=True)
    image = models.ImageField(upload_to = 'Images/%d%m%y')
    status = models.CharField(max_length=100, verbose_name='status', null=True, blank=True)

    def __str__(self):
        return self.name
        
class Varients(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, verbose_name='title', null=True, blank=True)
    availableStock = models.CharField(max_length=100, verbose_name='availableStock', null=True, blank=True)

    def __str__(self):
        return self.title