from rest_framework import serializers
from .models import Aplicacion

class AplicacionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Aplicacion
