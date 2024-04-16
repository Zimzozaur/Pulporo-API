from django.urls import path
from . import views


urlpatterns = [
    # Base
    path('', views.load_base, name='base'),

    # Views
    path('dashboard/', views.dashboard, name='dashboard'),

    path('ledger/', views.ListIOs.as_view(), name='ledger'),
    path('ledger/update-dom/', views.ListIOs.as_view(), name='ledger-update'),

    path('recurring/', views.recurring, name='recurring'),
    path('investments/', views.investments, name='investments'),
    path('liabilities/', views.liabilities, name='liabilities'),
    path('reminders/', views.reminders, name='reminders'),
    path('media/', views.media, name='media'),

    # Actions on OneIO
    path('create/oneio/', views.CreateIO.as_view(), name='create-io'),
    path('update/oneio/<int:pk>/', views.DetailIO.as_view(), name='detail-io'),
    path('delete/oneio/<int:pk>/', views.DeleteIO.as_view(), name='delete-io'),

    # Actions on Manager
    path('create/manager/<int:is_outcome>/', views.CreateIO.as_view(), name='create-manager'),
    path('update/manager/<int:pk>/', views.DetailIO.as_view(), name='detail-manager'),
    path('delete/manager/<int:pk>/', views.DeleteIO.as_view(), name='delete-manager'),

    # Actions on Investment
    path('create/investment/', views.CreateIO.as_view(), name='create-investment'),
    path('update/investment/<int:pk>/', views.DetailIO.as_view(), name='detail-investment'),
    path('delete/investment/<int:pk>/', views.DeleteIO.as_view(), name='delete-investment')

]


