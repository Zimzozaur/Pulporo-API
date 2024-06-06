from datetime import datetime

import pytest

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.response import Response

from django.urls import reverse
from django.utils import timezone
from django.db.models.query import QuerySet

from .models import Outflow, Inflow


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_outflow():
    return Outflow.objects.create(
        title='Test Outflow',
        value=100.50,
        date=datetime.now().date(),
        prediction=False,
        notes='Test notes'
    )


@pytest.fixture
def create_inflow():
    return Inflow.objects.create(
        title='Test Inflow',
        value=100.50,
        date=datetime.now().date(),
        notes='Test notes'
    )


@pytest.mark.django_db
def test_list_outflows(api_client, create_outflow):
    url = reverse('list-create-outflows')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['title'] == 'Test Outflow'


@pytest.mark.django_db
def test_create_outflow(api_client):
    url = reverse('list-create-outflows')
    data = {
        'title': 'New Outflow',
        'value': 200.75,
        'date': datetime.now().date(),
        'prediction': True,
        'notes': 'New test notes'
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Outflow.objects.count() == 1
    assert Outflow.objects.get().title == 'New Outflow'


@pytest.mark.django_db
def test_list_inflows(api_client, create_inflow):
    url = reverse('list-create-inflows')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['title'] == 'Test Inflow'


@pytest.mark.django_db
def test_create_outflow(api_client):
    url = reverse('list-create-inflows')
    data = {
        'title': 'New Inflow',
        'value': 200.75,
        'date': datetime.now().date(),
        'notes': 'New test notes'
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Inflow.objects.count() == 1
    assert Inflow.objects.get().title == 'New Inflow'

