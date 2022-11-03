from django.db import transaction
from rest_framework import viewsets, response, status
from django.shortcuts import render
from rest_framework.decorators import action

from carts.models import Cart

from .models import Brand, Product, Item
from .serializers import BrandSerializer, ProductSerializer, ItemSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


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
        """добавление item в корзину"""
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
