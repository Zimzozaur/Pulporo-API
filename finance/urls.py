from django.urls import path

from . import views

urlpatterns = [
    # Test Images for Textual
    path('images/', views.ImagesURLs.as_view(), name='base'),

    # Actions on OneIO
    path('outflows/', views.ListCreateOutflows.as_view(), name='outflows'),
    path('outflows/<int:pk>/', views.ReadUpdateDeleteOutflows.as_view(), name='outflows-pk'),

    path('inflows/', views.ListCreateInflows.as_view(), name='inflows'),
    path('inflows/<int:pk>/', views.ReadUpdateDeleteOutflows.as_view(), name='inflows-pk'),
]

