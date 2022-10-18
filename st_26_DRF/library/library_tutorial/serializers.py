from rest_framework import serializers

from .models import Author, Book


# class AuthorSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     first_name = serializers.CharField(max_length=50)
#     last_name = serializers.CharField(max_length=100)
#     photo = serializers.ImageField(required=False)
#     address = serializers.CharField(max_length=150)
#
#     def create (self, validate_data):
#         return Author.objects.create(**validate_data)
#         # return Author.objects.create(first_name="AAA", last_name="BBB", address="CCC")
#
#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get("first_name")
#         instance.last_name = validated_data.get("last_name")
#         instance.photo = validated_data.get("photo")
#         instance.address = validated_data.get("address")
#         instance.save()
#         return instance


author_data = {
    "first_name": "AAA",
    "last_name": "BBB",
    "address": "CCC",
}


class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Author
        fields = (
            "id",
            "first_name",
            "last_name",
            "address"
        )
