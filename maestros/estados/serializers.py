from rest_framework import serializers
from .models import Estado

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ('desc_estado','ind_estado',)
