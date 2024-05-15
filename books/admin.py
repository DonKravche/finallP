from django.contrib import admin
from .models import Book, Author, Genre, BookCheckout


# Register Author and Genre models without customization
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


# Custom admin class for a Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'author', 'genre', 'publication_date', 'stock_quantity', 'times_checked_out', 'available_copies',
        'checked_out_copies')
    list_filter = ('author', 'genre')
    search_fields = ('title', 'author__first_name', 'author__last_name')

    def times_checked_out(self, obj):
        return obj.checkouts.count()

    def available_copies(self, obj):
        return obj.stock_quantity - obj.checkouts.filter(return_date__isnull=True).count()

    def checked_out_copies(self, obj):
        return obj.checkouts.filter(return_date__isnull=True).count()

    times_checked_out.short_description = 'Times Checked Out'
    available_copies.short_description = 'Available Copies'
    checked_out_copies.short_description = 'Checked Out Copies'
