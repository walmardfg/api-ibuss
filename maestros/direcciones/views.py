from django.shortcuts import render

from rest_framework import generics
from .models import Direccion
from .serializers import DireccionSerializer

class DireccionList(generics.ListCreateAPIView):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class DireccionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
