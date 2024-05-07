from django.urls import path
from . import views


urlpatterns = [
    # Base
    path('images/', views.ImagesURLs.as_view(), name='base'),

    # Actions on OneIO
    path('get/oneio/<int:is_outcome>/', views.CreateIO.as_view(), name='get-OneIO-form'),
    path('post/oneio/<int:is_outcome>/', views.CreateIO.as_view(), name='post-OneIO-form'),


]


