from datetime import datetime

import pytest

from rest_framework import status
from rest_framework.test import APIClient

from django.urls import reverse
from .models import Outflow, Inflow
from .serializers import OutflowFullSerializer, InflowFullSerializer

LIST_CREATE_OUTFLOWS: str = reverse('list-post-outflow')
LIST_CREATE_INFLOWS: str = reverse('list-post-inflow')
READ_UPDATE_DELETE_OUTFLOW_ONE: str = reverse(
    'get-put-delete-outflow', kwargs={'pk': 1}
)
READ_UPDATE_DELETE_INFLOW_ONE: str = reverse(
    'get-put-delete-inflow',
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

############################
# Testing ListPostOutflows #
############################


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


###########################
# Testing ListPostInflows #
###########################

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


####################################
# Testing ReadUpdateDeleteOutflows #
####################################


@pytest.mark.django_db
def test_get_outflow(api_client, create_outflow):
    response = api_client.get(READ_UPDATE_DELETE_OUTFLOW_ONE)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == len(OutflowFullSerializer.Meta.fields)
    assert response.data['title'] == 'Test Outflow'


@pytest.mark.django_db
def test_patch_outflow(api_client, create_outflow):
    update = {'title': 'Happy Outflow'}
    response = api_client.get(READ_UPDATE_DELETE_OUTFLOW_ONE)
    assert response.data['title'] == 'Test Outflow'
    response = api_client.patch(READ_UPDATE_DELETE_OUTFLOW_ONE, update)
    assert response.data['title'] == 'Happy Outflow'


@pytest.mark.django_db
def test_delete_outflow(api_client, create_outflow):
    assert len(Outflow.objects.all()) == 1
    response = api_client.delete(READ_UPDATE_DELETE_OUTFLOW_ONE)
    assert len(Outflow.objects.all()) == 0
    assert response.status_code == status.HTTP_204_NO_CONTENT

####################################
# Testing ReadUpdateDeleteOutflows #
####################################


@pytest.mark.django_db
def test_get_inflow(api_client, create_inflow):
    response = api_client.get(READ_UPDATE_DELETE_INFLOW_ONE)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == len(InflowFullSerializer.Meta.fields)
    assert response.data['title'] == 'Test Inflow'


@pytest.mark.django_db
def test_patch_outflow(api_client, create_inflow):
    update = {'title': 'Happy Inflow'}
    response = api_client.get(READ_UPDATE_DELETE_INFLOW_ONE)
    assert response.data['title'] == 'Test Inflow'
    response = api_client.patch(READ_UPDATE_DELETE_INFLOW_ONE, update)
    assert response.data['title'] == 'Happy Inflow'


@pytest.mark.django_db
def test_delete_outflow(api_client, create_inflow):
    assert len(Inflow.objects.all()) == 1
    response = api_client.delete(READ_UPDATE_DELETE_INFLOW_ONE)
    assert len(Inflow.objects.all()) == 0
    assert response.status_code == status.HTTP_204_NO_CONTENT
