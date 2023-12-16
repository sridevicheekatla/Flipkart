from rest_framework import serializers
from .models import RelaxedFit, RegularFit


class RelaxedFitSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelaxedFit
        fields = '__all__'


class RegularFitSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegularFit
        fields = '__all__'
