from rest_framework import serializers
from .models import Ciudad

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('id_municipio','desc_ciudad','cod_postal','ind_capital','ind_estado',)
