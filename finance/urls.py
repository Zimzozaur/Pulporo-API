from django.urls import path

from . import views

urlpatterns = [
    # Test Images for Textual
    path('images/', views.ImagesURLs.as_view(), name='base'),

    # Actions on OneIO
    path('outflows/', views.ListPostOutflows.as_view(), name='list-post-outflow'),
    path(
        'outflows/<int:pk>/',
        views.GetPutDeleteOutflow.as_view(),
        name='get-put-delete-outflow'
    ),

    path('inflows/', views.ListPostInflows.as_view(), name='list-post-inflow'),
    path(
        'inflows/<int:pk>/',
        views.GetPutDeleteInflow.as_view(),
        name='get-put-delete-inflow'
    ),
]
