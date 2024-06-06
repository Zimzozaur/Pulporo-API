from datetime import datetime

import pytest

from rest_framework import status
from rest_framework.test import APIClient

from django.urls import reverse
from .models import Outflow, Inflow
from .serializers import OutflowFullSerializer

LIST_CREATE_OUTFLOWS: str = reverse('list-create-outflows')
LIST_CREATE_INFLOWS: str = reverse('list-create-inflows')
READ_UPDATE_DELETE_OUTFLOWS_ONE: str = reverse(
    'read-update-delete-outflows', kwargs={'pk': 1}
)
READ_UPDATE_DELETE_INFLOWS_ONE: str = reverse(
    'read-update-delete-inflows',
    kwargs={'pk': 1}
)

EXAMPLE_OUTFLOW: dict = {
    'title': 'New Outflow',
    'value': 200.75,
    'date': datetime.now().date(),
    'prediction': True,
    'notes': 'New test notes'
}

EXAMPLE_INFLOW: dict = {
    'title': 'New Inflow',
    'value': 200.75,
    'date': datetime.now().date(),
    'notes': 'New test notes'
}


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
    response = api_client.get(LIST_CREATE_OUTFLOWS)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['title'] == 'Test Outflow'


@pytest.mark.django_db
def test_create_outflow(api_client):
    response = api_client.post(LIST_CREATE_OUTFLOWS, EXAMPLE_OUTFLOW, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Outflow.objects.count() == 1
    assert Outflow.objects.get().title == 'New Outflow'


@pytest.mark.django_db
def test_list_inflows(api_client, create_inflow):
    response = api_client.get(LIST_CREATE_INFLOWS)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['title'] == 'Test Inflow'


@pytest.mark.django_db
def test_create_inflow(api_client):
    response = api_client.post(LIST_CREATE_INFLOWS, EXAMPLE_INFLOW, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Inflow.objects.count() == 1
    assert Inflow.objects.get().title == 'New Inflow'


@pytest.mark.django_db
def test_get_outflow(api_client, create_outflow):
    response = api_client.get(READ_UPDATE_DELETE_OUTFLOWS_ONE)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == len(OutflowFullSerializer.Meta.fields)
    assert response.data['title'] == 'Test Outflow'


@pytest.mark.django_db
def test_patch_outflow(api_client, create_outflow):
    update = {'title': 'Happy Outflow'}
    response = api_client.get(READ_UPDATE_DELETE_OUTFLOWS_ONE)
    assert response.data['title'] == 'Test Outflow'
    response = api_client.patch(READ_UPDATE_DELETE_OUTFLOWS_ONE, update)
    assert response.data['title'] == 'Happy Outflow'


@pytest.mark.django_db
def test_put_outflow(api_client):
    assert len(Outflow.objects.all()) == 0
    response = api_client.put(READ_UPDATE_DELETE_OUTFLOWS_ONE, EXAMPLE_OUTFLOW)
    print(response.data)
    assert len(Outflow.objects.all()) == 1



