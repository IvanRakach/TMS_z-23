from rest_framework import serializers

from .models import Product, Item
# from brands.serializers import BrandSerializer


class ProductSerializer(serializers.ModelSerializer):
    # brand = BrandSerializer()

    class Meta:
        model = Product
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Item
        fields = '__all__'
