from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import DetMiscelaneo
from .serializers import DetMiscelaneoSerializer

class DetMiscelaneoList(generics.ListCreateAPIView):
    queryset = DetMiscelaneo.objects.all()
    serializer_class = DetMiscelaneoSerializer

class DetMiscelaneoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetMiscelaneo.objects.all()
    serializer_class = DetMiscelaneoSerializer