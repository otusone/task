from rest_framework import serializers
from .models import Product, Varients


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'class_name', 'price', 'status', 'image']

class AddVarientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Varients
        fields = ['title', 'availableStock']

