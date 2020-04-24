from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Sucursal
from .serializers import SucursalSerializer

class SucursalList(generics.ListCreateAPIView):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer

class SucursalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer