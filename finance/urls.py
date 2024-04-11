from django.urls import path
from .views import ListIOs, DetailIO, CreateIO, DeleteIO
from .views import dashboard, recurring, investments, liabilities, reminders, media


urlpatterns = [
    # Views
    path('dashboard/', dashboard, name='dashboard'),
    path('ledger/', ListIOs.as_view(), name='ledger'),
    path('recurring/', recurring, name='recurring'),
    path('investments/', investments, name='investments'),
    path('liabilities/', liabilities, name='liabilities'),
    path('reminders/', reminders, name='reminders'),
    path('media/', media, name='media'),

    # Actions on OneIO
    path('create/oneio/<int:is_outcome>/', CreateIO.as_view(), name='create-io'),
    path('update/oneio/<int:pk>/', DetailIO.as_view(), name='detail-io'),
    path('delete/oneio/<int:pk>/', DeleteIO.as_view(), name='delete-io'),

    # Actions on Manager
    path('create/manager/<int:is_outcome>/', CreateIO.as_view(), name='create-manager'),
    path('update/manager/<int:pk>/', DetailIO.as_view(), name='detail-manager'),
    path('delete/manager/<int:pk>/', DeleteIO.as_view(), name='delete-manager'),

    # Actions on Investment
    path('create/investment/', CreateIO.as_view(), name='create-investment'),
    path('update/investment/<int:pk>/', DetailIO.as_view(), name='detail-investment'),
    path('delete/investment/<int:pk>/', DeleteIO.as_view(), name='delete-investment')

]


