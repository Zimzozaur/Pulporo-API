from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.generics import (
    ListCreateAPIView, GenericAPIView
)

from django.utils import timezone
from django.db.models import QuerySet

from .models import Outflow, Inflow
from . import serializers


class GetPatchDeleteAPIView(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            GenericAPIView):
    """
    Concrete view for retrieving, updating or deleting a model instance.
    """

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ImagesURLs(APIView):
    JSON = {
        1: "https://www.apple.com/v/mac-studio/f/images/overview/hero/static_front__fmvxob6uyxiu_large.jpg",
        2: "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/mac-pro-tower-hero-splitter-2023?wid"
           "=904&hei=840&fmt=jpeg&qlt=90&.v=1684181485853",
        3: "https://www.apple.com/v/displays/a/images/overview/hero/hero__fkyiyagbj7yy_large.jpg",
        4: "https://www.apple.com/v/displays/a/images/overview/routers/mac_for_you__95lbzl9lp36e_large.jpg",
    }

    def get(self, request: Request) -> Response:
        return Response(self.JSON)


class ListPostOneBaseView(ListCreateAPIView):
    """Base class for Inflows and Outflows to return list of them"""
    model = None
    serializer_class = None

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


class GetPutDeleteOneBaseView(GetPatchDeleteAPIView):
    queryset = None
    serializer_class = None


class ListPostOutflows(ListPostOneBaseView):
    """Return list of Outflows"""
    model = Outflow
    serializer_class = serializers.OutflowListSerializer


class ListPostInflows(ListPostOneBaseView):
    """Return list of Inflows"""
    model = Inflow
    serializer_class = serializers.InflowListSerializer


class GetPutDeleteOutflow(GetPutDeleteOneBaseView):
    queryset = Outflow.objects.all()
    serializer_class = serializers.OutflowFullSerializer


class GetPutDeleteInflow(GetPutDeleteOneBaseView):
    queryset = Inflow.objects.all()
    serializer_class = serializers.InflowFullSerializer

