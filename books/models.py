from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from accounts.models import CustomUser


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books')
    publication_date = models.DateField()
    stock_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class BookCheckout(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='checkouts')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='book_checkouts')
    checkout_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
