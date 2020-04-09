from rest_framework import serializers
from .models import DetMiscelaneo

class DetMiscelaneoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetMiscelaneo
        fields = '__all__'
