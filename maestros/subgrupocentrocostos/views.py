from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import SubGrupoCentroCosto
from .serializers import SubGrupoCentroCostoSerializer

class SubGrupoCentroCostoList(generics.ListCreateAPIView):
    queryset = SubGrupoCentroCosto.objects.all()
    serializer_class = SubGrupoCentroCostoSerializer

class SubGrupoCentroCostoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubGrupoCentroCosto.objects.all()
    serializer_class = SubGrupoCentroCostoSerializer