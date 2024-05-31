from django.urls import path
from . import views


urlpatterns = [
    # Base
    path('images/', views.ImagesURLs.as_view(), name='base'),

    # Actions on OneIO
    path('outflows/', views.OneOffOutflowsView.as_view(), name='outflows'),
    path('inflows/', views.OneOffInflowsView.as_view(), name='inflows')
]


