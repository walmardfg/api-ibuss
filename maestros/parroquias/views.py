from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Parroquia
from .serializers import ParroquiaSerializer

class ParroquiaList(generics.ListCreateAPIView):
    queryset = Parroquia.objects.all()
    serializer_class = ParroquiaSerializer

class ParroquiaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parroquia.objects.all()
    serializer_class = ParroquiaSerializer