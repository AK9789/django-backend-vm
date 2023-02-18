from rest_framework import serializers
from .models import Tpp

class TppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tpp
        fields = '__all__'