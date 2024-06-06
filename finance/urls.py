from django.urls import path
from .views import (
    ListCreateOutflows, ReadUpdateDeleteOutflows,
    ListCreateInflows
)


urlpatterns = [
    # Actions on OneIO
    path('outflows/', ListCreateOutflows.as_view(), name='outflows'),
    path('outflows/<int:pk>/', ReadUpdateDeleteOutflows.as_view(), name='outflows-pk'),
    path('inflows/', ListCreateInflows.as_view(), name='inflows')
]

