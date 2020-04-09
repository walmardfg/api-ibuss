from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Miscelaneo
from .serializers import MiscelaneoSerializer

class MiscelaneoList(generics.ListCreateAPIView):
    queryset = Miscelaneo.objects.all()
    serializer_class = MiscelaneoSerializer

class MiscelaneoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Miscelaneo.objects.all()
    serializer_class = MiscelaneoSerializer