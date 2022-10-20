from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer  # передаем класс сериализатора


# класс APIView стоит во главе всех классов представления APIView
# (базовый функционал в рамках джанго рест фреймворк)
class WomenAPIView (APIView):
    # def get(self, request):
    #     return Response({"title": "Angelina"})  # Response - класс, кот преобр-т словарь в json строку

    def get(self, request):
        """
        Получим записи из БД через get запрос
        :param request:
        :return:
        """
        # lst = Women.objects.all().values()  # получаем не просто кверисет, а набор конкретных значений
        lst = Women.objects.all()
        # return Response({"posts_from_DB": list(lst)})
        # many=True - обработка не одной записи, а списка записей, Т.Е. получаем СПИСОК
        # .data - СПИСОК преобразовываем в словарь
        return Response({"posts_from_DB": WomenSerializer(lst, many=True).data})

    # def post(self, request):
    #     return Response({"title": "Jennifer"})

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Women.objects.create(
            title=request.data["title"],
            content=request.data["content"],
            cat_id=request.data["cat_id"],
        )
        return Response({"post": WomenSerializer(post_new).data})
