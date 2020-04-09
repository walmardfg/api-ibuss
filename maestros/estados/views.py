from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Estado
from .serializers import EstadoSerializer

class EstadoList(generics.ListCreateAPIView):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class EstadoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer