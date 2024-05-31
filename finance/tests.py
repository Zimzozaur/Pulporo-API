from datetime import datetime

import pytest

from django.urls import reverse
from django.utils import timezone

from rest_framework.test import APIClient
from rest_framework.response import Response

from .models import Outflow


@pytest.mark.django_db
class TestOneOffOutflowsView:
    url: str = reverse('outflows')
    example_fixture: dict = {
        'title': 'Mario in DB',
        'value': '123.45',
        'date': datetime.now().strftime('%Y-%m-%d'),
        'prediction': True,
        'notes': ''
    }
    api_client: APIClient = APIClient()

    def test_get_request_empty_DB(self):
        response: Response = self.api_client.get(self.url)
        assert response.status_code == 200
        assert response.data == []

    def test_get_request_one_record_DB(self):
        Outflow.objects.create(**self.example_fixture)
        response: Response = self.api_client.get(self.url)
        assert response.data == [self.example_fixture]

    def test_get_request_one_record_DB_current_date(self):
        Outflow.objects.create(**self.example_fixture)
        params = {
            'year': timezone.now().year,
            'month': timezone.now().month
        }
        response: Response = self.api_client.get(self.url, params)
        assert response.data == [self.example_fixture]

    def test_get_request_one_record_DB_not_current(self):
        Outflow.objects.create(**self.example_fixture)
        params = {
            'year': timezone.now().year,
            'month': 1
        }
        response: Response = self.api_client.get(self.url, params)
        assert response.data == []


