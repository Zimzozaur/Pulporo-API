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

    # Actions
    path('create/', CreateIO.as_view(), name='create-io'),
    path('update/<int:pk>/', DetailIO.as_view(), name='detail-io'),
    path('delete/<int:pk>', DeleteIO.as_view(), name='delete-io')
]


