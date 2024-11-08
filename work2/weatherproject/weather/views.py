from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Weather
from .serializers import WeatherSerializer


# Create your views here.

class TopView(ListView):
    model = Weather
    template_name = "top.html"

class WeatherAPIView(RetrieveAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = [IsAuthenticated]