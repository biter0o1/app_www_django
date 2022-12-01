from rest_framework import serializers
from .models import Wklejki


class WklejkiSerializer(serializers.Serializer):
    class Meta:
        model = Wklejki
        fields = ['__all__']

