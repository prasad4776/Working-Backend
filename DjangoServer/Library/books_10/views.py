from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Book
from .serializers import BookSerializer
import json

@csrf_exempt
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        books_serializer = BookSerializer(books, many=True)
        return JsonResponse(books_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        print(request)
        print(request.body)
        json_body = json.loads(request.body)
        print(json_body)

        book_serializer = BookSerializer(data=json_body)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse(book_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Book.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        book_serializer = BookSerializer(book)
        return JsonResponse(book_serializer.data)

    elif request.method == 'PUT':
        book_data = JSONParser().parse(request)
        book_serializer = BookSerializer(book, data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse(book_serializer.data)
        return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        book.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def book_list_age(request, price):
    books = Book.objects.filter(price=price)

    if request.method == 'GET':
        book_serializer = BookSerializer(books, many=True)
        return JsonResponse(book_serializer.data, safe=False)
