from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Parametro
from .serializers import ParametroSerializer

class ParametroList(generics.ListCreateAPIView):
    queryset = Parametro.objects.all()
    serializer_class = ParametroSerializer

class ParametroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parametro.objects.all()
    serializer_class = ParametroSerializer