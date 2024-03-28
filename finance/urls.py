from django.urls import path
from .views import ListIOs, DetailIO, UpdateIO


urlpatterns = [
    path('', ListIOs.as_view(), name='list-io'),
    path('detail/<int:pk>/', DetailIO.as_view(), name='detail-io'),
    path('update/<int:pk>/', UpdateIO.as_view(), name='update-io'),
]
