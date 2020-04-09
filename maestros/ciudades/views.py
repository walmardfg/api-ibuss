from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Ciudad
from .serializers import CiudadSerializer

class CiudadList(generics.ListCreateAPIView):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer

class CiudadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer