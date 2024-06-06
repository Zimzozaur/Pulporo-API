from rest_framework import serializers

from .models import Outflow, Inflow


class OutflowSerializer(serializers.ModelSerializer[Outflow]):
    class Meta:
        model = Outflow
        fields = ['id', 'title', 'value', 'date', 'prediction', 'notes', 'creation_date', 'last_modification']


class InflowSerializer(serializers.ModelSerializer[Inflow]):
    class Meta:
        model = Inflow
        fields = ['id', 'title', 'value', 'date', 'notes', 'creation_date', 'last_modification']


