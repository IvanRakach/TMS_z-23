import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women

# Определим класс объекты которого будем сериализовать,
# т.е. преобразовывать в JSON строку.
# этот класс будет имитировать работу модели фреймворка Django
# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        # обращаемся к интересующей модели через менеджер и метод создания и
        # передаем словарь из ПРОВЕРЕННЫХ данных,
        # который приходит от клиента через POST запрос
        return Women.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance - это ссылка на объект модели Women
        # validated_data - это словарь из ПРОВЕРЕННЫХ данных,
        # которые нужно изменить в БД
        # -----
        # обращаемся к полю объекта модели через instance.title
        # обращаемся к данным клиента и берем их через ключ "title",
        # а если мы не можем взять ключ "title", то возвращаем имеющиеся значения title
        # такую процедуру делаем для всех полей модели кроме "time_create"
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        # когда мы просмотрели все данные мы можем сохранить все данные
        instance.save()
        return instance

    def delete(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        # когда мы просмотрели все данные мы можем сохранить все данные
        instance.delete()
        return instance

# def encode():
#     """
#     Преобразование объектов класса (модели) в JSON строку для передачи клиенту
#     :return:JSON строка
#     """
#     model = WomenModel("Angelina Jolie", "Content: Angelina Jolie")
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep="\n")
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     """
#     Обратное преобразование из JSON строки в объект класса WomenModel
#     :return: объект сериализатора
#     """
#     # осуществляем имитацию получения информации от клиента через "io.BytesIO"
#     stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"Content: Angelina Jolie"}')
#     # Далее для формирования словаря мы воспользуемся JSON парсером
#     data = JSONParser().parse(stream)
#     # Далее используем сериализатор с именованным параметром "data" и
#     # получаем объект сериализатора
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)

# class WomenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Women
#         fields = ("title", "cat_id")  # поля которые отправляются обратно пользователю
