from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Pais
from .serializers import PaisSerializer

class PaisList(generics.ListCreateAPIView):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

class PaisDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer