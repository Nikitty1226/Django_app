from django.contrib import admin
from django.urls import path
from .views import helloworldappview

urlpatterns = [
    path('helloworldapp/', helloworldappview),
]