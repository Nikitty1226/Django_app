from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.generics import ListCreateAPIView
from .models import Book
from .serializer import BookSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ListView(ListView):
    template_name = 'list.html'
    model = Book

class BookListAPI(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]