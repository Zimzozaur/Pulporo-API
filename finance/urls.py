from django.urls import path

from . import views

urlpatterns = [
    # Test Images for Textual
    path('images/', views.ImagesURLs.as_view(), name='base'),

    # Actions on OneIO
    path('outflows/', views.ListPostOutflows.as_view(), name='list-create-outflows'),
    path(
        'outflows/<int:pk>/',
        views.ReadUpdateDeleteOutflows.as_view(),
        name='read-update-delete-outflows'
    ),

    path('inflows/', views.ListPostInflows.as_view(), name='list-create-inflows'),
    path(
        'inflows/<int:pk>/',
        views.ReadUpdateDeleteOutflows.as_view(),
        name='read-update-delete-inflows'
    ),
]
