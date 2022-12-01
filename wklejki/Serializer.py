from rest_framework import serializers
from .models import Wklejki


class WklejkiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wklejki
        fields ='__all__'
