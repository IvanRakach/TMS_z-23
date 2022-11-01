from django.db import transaction
from rest_framework import viewsets, response, status
from rest_framework.decorators import action
from django.shortcuts import render

from users.models import Cart
from users.serializers import CartSerializer

from .models import Product, Item
from .serializers import ProductSerializer, ItemSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @transaction.atomic
    @action(
        detail=True,  # конкретный товар
        methods=['POST'],
        url_path='add-to-cart'
    )
    def add_item_to_cart(self, request, pk=None):
        """добавление item в корзинц"""
        print(request.user)
        cart, _ = Cart.objects.get_or_create(user=request.user)  # get_or_create отдает tuple; создан ли объект
        print(cart)
        print(_)
        item = self.get_object()
        cart.items.add(item)
        print(item)
        return response.Response(status=status.HTTP_200_OK)
        # raise Exception('hello')

    @action(
        detail=False,  # конкретный товар
        methods=['GET'],
        url_path='cart'
    )
    def cart(self, request):
        """получение всех item"""
        cart, _ = Cart.objects.get_or_create(user=request.user)
        serializer = ItemSerializer(cart.items.all(), many=True)
        return response.Response(serializer.data)
