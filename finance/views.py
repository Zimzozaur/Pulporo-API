from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView
)

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.decorators.http import require_GET
from django.utils import timezone
from django.urls import reverse_lazy
from django.db.models import Sum

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


class ListInflows(ListAPIView):
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        year = self.request.query_params.get('year', timezone.now().year)
        month = self.request.query_params.get('month', timezone.now().month)

        return queryset.filter(date__year=year, date__month=month)



class ListOutflows(ListAPIView):
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        year = self.request.query_params.get('year', timezone.now().year)
        month = self.request.query_params.get('month', timezone.now().month)

        return queryset.filter(date__year=year, date__month=month)




