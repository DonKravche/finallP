from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_, name='login'),

    path('home/', views.home, name='home'),
    path('logout/', views.logout_, name='logout'),
]