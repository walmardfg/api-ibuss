from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Moneda
from .serializers import MonedaSerializer

class MonedaList(generics.ListCreateAPIView):
    queryset = Moneda.objects.all()
    serializer_class = MonedaSerializer

class MonedaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Moneda.objects.all()
    serializer_class = MonedaSerializer