from django.urls import path
from .views import ReserveBookView

urlpatterns = [
    path('reserve/<int:book_id>/', ReserveBookView.as_view(), name='reserve_book'),
]