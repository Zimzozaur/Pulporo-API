from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView
)

from django.utils import timezone

from .models import Outflow, Inflow
from .serializers import (
    OutflowSerializer,
    InflowSerializer,
)


class ImagesURLs(APIView):
    JSON = {
        1: "https://www.apple.com/v/mac-studio/f/images/overview/hero/static_front__fmvxob6uyxiu_large.jpg",
        2: "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/mac-pro-tower-hero-splitter-2023?wid=904&hei=840&fmt=jpeg&qlt=90&.v=1684181485853",
        3: "https://www.apple.com/v/displays/a/images/overview/hero/hero__fkyiyagbj7yy_large.jpg",
        4: "https://www.apple.com/v/displays/a/images/overview/routers/mac_for_you__95lbzl9lp36e_large.jpg",
    }

    def get(self, request):
        return Response(self.JSON)


class FlowsBaseView(ListCreateAPIView):
    """Base class for Inflows and Outflows to return list of them"""
    model = None
    serializer_class = None

    def get_queryset(self):
        if self.model is None:
            raise NotImplementedError("model attribute must be set for the view.")
        if self.serializer_class is None:
            raise NotImplementedError("serializer_class attribute must be set for the view.")

        queryset = self.model.objects.all()

        year = self.request.query_params.get('year', timezone.now().year)
        month = self.request.query_params.get('month', timezone.now().month)

        res = queryset.filter(date__year=year, date__month=month)

        return res


class OneOffInflowsView(FlowsBaseView):
    """Return list of Inflows"""
    model = Inflow
    serializer_class = InflowSerializer


class OneOffOutflowsView(FlowsBaseView):
    """Return list of Outflows"""
    model = Outflow
    serializer_class = OutflowSerializer


