from django.urls import path
from .views import ListIOs, DetailIO


urlpatterns = [
    path('', ListIOs.as_view(), name='list-io'),
    path('deatil/<int:pk>', DetailIO.as_view(), name='detail-io')
]
