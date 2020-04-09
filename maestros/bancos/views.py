from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Banco
from .serializers import BancoSerializer

class BancoList(generics.ListCreateAPIView):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer

class BancoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer