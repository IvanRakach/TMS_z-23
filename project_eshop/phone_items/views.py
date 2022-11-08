from django.db import transaction
from rest_framework import viewsets, response, status, generics
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from carts.models import Cart

from .models import Brand, Product, Item
from .serializers import BrandSerializer, ProductSerializer, ItemSerializer


def index(request):
    latest_products = Item.objects.order_by('-time_create')[:4]
    param_for_render = {
        'title': 'Главная страница',
        'latest_products': latest_products,
    }
    return render(request, 'phone_items/index.html', context=param_for_render)


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# --------------------------------------------------------------------------------#
class ProductAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'phone_items/products_list.html'

    def get(self, request):
        products = Product.objects.all()
        # profile = get_object_or_404(Profile, pk=pk)
        serializer = ProductSerializer(products)
        return Response({'serializer': serializer, 'products': list(products)})

    # def post(self, request, pk):
    #     profile = get_object_or_404(Profile, pk=pk)
    #     serializer = ProfileSerializer(profile, data=request.data)
    #     if not serializer.is_valid():
    #         return Response({'serializer': serializer, 'profile': profile})
    #     serializer.save()
    #     return response.redirect('profile-list')


class ProductAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'phone_items/products_list.html'

    def get(self, request):
        """
        Получим записи из БД через get запрос
        :param request:
        :return:
        """
        # lst = Women.objects.all().values()  # получаем не просто кверисет, а набор конкретных значений
        products = Product.objects.all()
        # return Response({"posts_from_DB": list(lst)})
        # many=True - обработка не одной записи, а списка записей, Т.Е. получаем СПИСОК
        # .data - СПИСОК преобразовываем в словарь
        serializer = ProductSerializer(products, many=True).data
        return Response({'serializer': serializer, 'products': list(products)})
# --------------------------------------------------------------------------------#

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
        # print(request.user)
        cart, _ = Cart.objects.get_or_create(user=request.user)  # get_or_create отдает tuple; создан ли объект
        # print(cart)
        # print(_)
        item = self.get_object()
        cart.items.add(item)
        # print(item)
        return response.Response(status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=['GET'],
        url_path='cart'
    )
    def cart(self, request):
        """получение всех item"""
        cart, _ = Cart.objects.get_or_create(user=request.user)
        serializer = ItemSerializer(cart.items.all(), many=True)
        return response.Response(serializer.data)
