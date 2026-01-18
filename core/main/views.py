from django.shortcuts import render
from rest_framework import viewsets
from main.models import Car
from main.serializers import CarSerializer
# Create your views here.

class CarApiRead(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer