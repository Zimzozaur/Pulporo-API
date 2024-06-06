from rest_framework.serializers import Serializer
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView, UpdateAPIView, DestroyAPIView
)

from django.utils import timezone
from django.db.models import QuerySet, Model

from .models import Outflow, Inflow
from .serializers import (
    OutflowSerializer,
    InflowSerializer,
)


class ListCreateFlowsBaseView(ListCreateAPIView):
    """Base class for Inflows and Outflows to return list of them"""
    model = Model
    serializer_class = Serializer

    def get_queryset(self) -> QuerySet:
        if self.model is None:
            raise NotImplementedError("model attribute must be set for the view.")
        if self.serializer_class is None:
            raise NotImplementedError("serializer_class attribute must be set for the view.")

        queryset = self.model._default_manager.all()

        year = self.request.query_params.get('year', timezone.now().year)
        month = self.request.query_params.get('month', timezone.now().month)

        res = queryset.filter(date__year=year, date__month=month)

        return res


class ListCreateOutflows(ListCreateFlowsBaseView):
    """Return list of Outflows"""
    model = Outflow
    serializer_class = OutflowSerializer


class ListCreateInflows(ListCreateFlowsBaseView):
    """Return list of Inflows"""
    model = Inflow
    serializer_class = InflowSerializer


class ReadUpdateDeleteOutflows(RetrieveUpdateDestroyAPIView):
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer





