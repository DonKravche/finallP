from django.contrib.auth import login, logout
from django.contrib.sites import requests
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from accounts.forms import UserRegistrationForm, UserLoginForm

from django.contrib.auth.decorators import user_passes_test

from books.models import Book
import requests
from books.models import Book, BookCheckout


def home(request):
    # Make a request to your API endpoint
    response = requests.get('http://127.0.0.1:8000/books/api/books/')
    books = response.json()

    book_statuses = {}
    for book in books:
        book_id = book['id']
        checkouts = BookCheckout.objects.filter(book_id=book_id, return_date__isnull=True)
        if checkouts.exists():
            book_statuses[book_id] = 'reserved'
        else:
            book_statuses[book_id] = 'available'

    # Paginate the books
    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'book_statuses': book_statuses,
    }
    return render(request, 'home.html', context)


def login_user(request):
    form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_staff:
                return redirect('admin:index')
            else:
                return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def staff_check(user):
    return user.is_staff


@user_passes_test(staff_check, login_url='login')
def admin_view(request):
    # admin view code
    return render(request, 'admin.html')


def logout_(request):
    logout(request)
    return redirect('login')
