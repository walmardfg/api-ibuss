from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Compania
from .serializers import CompaniaSerializer

class CompaniaList(generics.ListCreateAPIView):
    queryset = Compania.objects.all()
    serializer_class = CompaniaSerializer

class CompaniaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Compania.objects.all()
    serializer_class = CompaniaSerializer