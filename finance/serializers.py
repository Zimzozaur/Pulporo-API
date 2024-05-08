from rest_framework import serializers


class BaseIOSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    value = serializers.DecimalField(max_digits=17, decimal_places=2)
    date = serializers.DateField()
    notes = serializers.CharField(allow_blank=True)


class OutflowSerializer(BaseIOSerializer):
    prediction = serializers.BooleanField(default=True)


class InflowSerializer(BaseIOSerializer):
    pass


