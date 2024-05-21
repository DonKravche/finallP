from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from books.models import Book, BookCheckout
from django.utils import timezone


# Create your views here.

class ReserveBookView(APIView):
    def post(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

        if book.stock_quantity <= 0:
            return Response({'error': 'Book is out of stock'}, status=status.HTTP_400_BAD_REQUEST)

        user = request.user
        if BookCheckout.objects.filter(book=book, user=user, return_date__isnull=True).exists():
            return Response({'error': 'You have already reserved this book'}, status=status.HTTP_400_BAD_REQUEST)

        checkout = BookCheckout.objects.create(book=book, user=user)
        return Response({'message': 'Book reserved successfully'}, status=status.HTTP_201_CREATED)