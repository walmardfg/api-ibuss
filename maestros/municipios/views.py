from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Municipio
from .serializers import MunicipioSerializer

class MunicipioList(generics.ListCreateAPIView):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer

class MunicipioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer