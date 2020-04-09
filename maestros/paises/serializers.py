from rest_framework import serializers
from .models import Pais

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('desc_pais','ind_estado',)
        model = Pais
