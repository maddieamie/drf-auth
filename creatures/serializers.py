from rest_framework import serializers
from .models import MagicalCreature

class MagicalCreatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagicalCreature
        fields = '__all__'
