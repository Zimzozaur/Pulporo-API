from django.urls import path
from . import views


urlpatterns = [
    # Base
    path('images/', views.ImagesURLs.as_view(), name='base'),

    # Actions on OneIO


    path('outflows/', views.ListOutflows.as_view()),
    path('inflows/', views.ListInflows.as_view())


]


