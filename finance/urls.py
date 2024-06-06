from django.urls import path
from .views import (
    ListCreateOutflows, ReadUpdateDeleteOutflows,
    ListCreateInflows, ImagesURLs
)


urlpatterns = [
    # Test Images for Textual
    path('images/', ImagesURLs.as_view(), name='base'),

    # Actions on OneIO
    path('outflows/', ListCreateOutflows.as_view(), name='outflows'),
    path('outflows/<int:pk>/', ReadUpdateDeleteOutflows.as_view(), name='outflows-pk'),
    path('inflows/', ListCreateInflows.as_view(), name='inflows')
]

