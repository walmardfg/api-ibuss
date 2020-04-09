from rest_framework import serializers
from .models import Parroquia

class ParroquiaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Parroquia
        fields = '__all__'
