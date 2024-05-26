from django.db.models import Count, OuterRef, Subquery, Q
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Book, BookCheckout
from accounts.models import CustomUser
from .serializers import BookSerializer


class BookStatsView(APIView):
    def get(self, request):
        # 1. The most popular 10 books (the most requested)
        most_popular_books = Book.objects.annotate(
            total_checkouts=Count('checkouts')
        ).order_by('-total_checkouts')[:10]
        most_popular_books_data = BookSerializer(most_popular_books, many=True).data

        # 2. How many times for each book in the last year they took out a book from the library
        one_year_ago = timezone.now() - timezone.timedelta(days=365)
        book_checkouts_last_year = BookCheckout.objects.filter(
            checkout_date__gte=one_year_ago
        ).values('book').annotate(
            total_checkouts=Count('id')
        ).order_by('book')
        book_checkouts_last_year_data = list(book_checkouts_last_year)

        # 3. Top 100 books that were most often returned late
        late_book_checkouts = Book.objects.annotate(
            late_count=Count(
                'checkouts',
                filter=Q(
                    checkouts__is_late=True
                )
            )
        ).order_by('-late_count')[:100]
        late_books = BookSerializer(late_book_checkouts, many=True).data

        # 4. Top 100 users who most often returned books late
        late_user_checkouts = CustomUser.objects.annotate(
            late_count=Count(
                'book_checkouts',
                filter=Q(
                    book_checkouts__is_returned=True,
                    book_checkouts__return_date__gt=Subquery(
                        BookCheckout.objects.filter(
                            user=OuterRef('pk'),
                            is_returned=True,
                        ).values('checkout_date')[:1]
                    )
                )
            )


        ).order_by('-late_count')[:100]
        late_users_data = [
            {
                'id': user.id,
                'username': user.username,
                'late_count': user.late_count
            }
            for user in late_user_checkouts
        ]

        stats = {
            'most_popular_books': most_popular_books_data,
            'book_checkouts_last_year': book_checkouts_last_year_data,
            'late_books': late_books,
            'late_users': late_users_data,
        }
        return Response(stats)
