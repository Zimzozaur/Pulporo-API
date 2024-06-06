from rest_framework import serializers

from .models import Outflow, Inflow


class OutflowListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outflow
        fields = ['id', 'title', 'value', 'date', 'prediction', 'notes']


class OutflowFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outflow
        fields = ['id', 'title', 'value', 'date', 'prediction', 'notes', 'creation_date', 'last_modification']


class InflowListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inflow
        fields = ['id', 'title', 'value', 'date', 'notes']


class InflowFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inflow
        fields = ['id', 'title', 'value', 'date', 'notes', 'creation_date', 'last_modification']


