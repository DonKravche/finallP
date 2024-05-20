from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser
from .models import Book, Author, Genre, BookCheckout

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Register Author and Genre models without customization
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


# admin.site.register(CustomUser)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'personal_number', 'birth_date')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'personal_number', 'birth_date',
            'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)


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
