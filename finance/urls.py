from django.urls import path
from .views import ListIOs, DetailIO, CreateIO, DeleteIO


urlpatterns = [
    path('ledger/', ListIOs.as_view(), name='ledger'),
    path('create/', CreateIO.as_view(), name='create-io'),
    path('update/<int:pk>/', DetailIO.as_view(), name='detail-io'),
    path('delete/<int:pk>', DeleteIO.as_view(), name='delete-io')
]


