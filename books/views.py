from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from .models import Book, Author, Genre, BookCheckout
from .serializers import (BookSerializer, AuthorSerializer, GenreSerializer, BookCheckoutSerializer,
                          BookCheckoutCreateSerializer, BookCheckoutUpdateSerializer)
from .filters import BookFilter

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookFilter


class BookCheckoutViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          mixins.UpdateModelMixin,
                          GenericViewSet):
    queryset = BookCheckout.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return BookCheckoutSerializer
        elif self.action == 'create':
            return BookCheckoutCreateSerializer
        elif self.action == 'update':
            return BookCheckoutUpdateSerializer
        return super().get_serializer_class()


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