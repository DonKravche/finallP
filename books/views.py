from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Book, Author, Genre
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000