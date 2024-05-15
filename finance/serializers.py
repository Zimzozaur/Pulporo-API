from rest_framework import serializers

from .models import Outflow, Inflow


class OutflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outflow
        fields = ['title', 'value', 'date', 'prediction', 'notes']


class InflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outflow
        fields = ['title', 'value', 'date', 'notes']


