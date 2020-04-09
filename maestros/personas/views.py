from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Persona
from .serializers import PersonaSerializer

class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class PersonaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer