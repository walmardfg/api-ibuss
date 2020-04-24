from rest_framework import serializers
from .models import GrupoCentroCosto

class GrupoCentroCostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoCentroCosto
        fields = '__all__'
