from rest_framework import serializers
from .models import SubGrupoCentroCosto

class SubGrupoCentroCostoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubGrupoCentroCosto
        fields = '__all__'
