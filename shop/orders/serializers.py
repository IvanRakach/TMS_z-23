from rest_framework import serializers

from .models import Order
from items.serializers import ItemSerializer


class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
