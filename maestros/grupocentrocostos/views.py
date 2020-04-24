from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import GrupoCentroCosto
from .serializers import GrupoCentroCostoSerializer

class GrupoCentroCostoList(generics.ListCreateAPIView):
    queryset = GrupoCentroCosto.objects.all()
    serializer_class = GrupoCentroCostoSerializer

class GrupoCentroCostoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GrupoCentroCosto.objects.all()
    serializer_class = GrupoCentroCostoSerializer

