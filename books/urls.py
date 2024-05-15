from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet, AuthorViewSet, GenreViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'genres', GenreViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]