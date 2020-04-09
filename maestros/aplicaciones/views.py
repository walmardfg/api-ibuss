from django.shortcuts import render

from rest_framework import generics
from .models import Aplicacion
from .serializers import AplicacionSerializer

class AplicacionList(generics.ListCreateAPIView):
    queryset = Aplicacion.objects.all()
    serializer_class = AplicacionSerializer

class AplicacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aplicacion.objects.all()
    serializer_class = AplicacionSerializer
