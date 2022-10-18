from django.shortcuts import render

from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Author
from .serializers import AuthorSerializer


class AuthorListView(APIView):
    """
    AuthorListView
    """
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)  # many=True - много авторов
        return Response(serializer.data)

    def post(self, request):
        # data = request.data  # это все данные запроса в body
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=201)
        return Response(serializer.errors, status=400)


class AuthorDetailsView(APIView):
    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNoExist as error:
            raise Http404

    def get(self, request, pk=None):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        author = self.get_object(pk)
        author.delete()
        return Response(status=204)

# делаем detailedview для конкретного объекта


# @api_view(["GET", "POST"])
# @csrf_exempt
# def authors_list_create_view(request):
#     if request.method == 'GET':
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)  # many=True - много авторов
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         # data = JSONParser().parse(request)
#         data = request.POST  # это все данные запроса в body
#         serializer = AuthorSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
