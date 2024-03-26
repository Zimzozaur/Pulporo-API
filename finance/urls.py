from django.urls import path
from .views import ReadIO


urlpatterns = [
    path('', ReadIO.as_view(), name='read-io'),
]
