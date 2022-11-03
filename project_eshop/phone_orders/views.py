from django.db import transaction
from rest_framework import viewsets, response, status
from rest_framework.decorators import action
from django.shortcuts import render

from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @transaction.atomic
    @action(
        detail=False,
        methods=['POST'],
        url_path='create'
    )
    def create_order(self, request):
        """создание заказа
        на этом этапе можно скинуть галку
        сделать подсчет
        """
        cart = request.user.cart  # получаем корзину пользователя

        # создаем ордер; закидываем item в заказ
        order = Order.objects.create(user=request.user)
        order.items.set(cart.items.all())

        cart.items.clear()  # чистим корзину

        serializer = self.get_serializer(order)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
