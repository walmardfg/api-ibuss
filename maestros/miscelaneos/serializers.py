from rest_framework import serializers
from .models import Miscelaneo

class MiscelaneoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Miscelaneo