from rest_framework import serializers
from .models import Direccion

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Direccion
