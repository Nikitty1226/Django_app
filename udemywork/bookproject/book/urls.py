from django.urls import path
from .views import ListView, BookListAPI

urlpatterns = [
    path('list/', ListView.as_view()),
    path('api/', BookListAPI.as_view()),
]

