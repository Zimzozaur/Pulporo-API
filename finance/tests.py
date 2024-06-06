from datetime import datetime

import pytest

from django.urls import reverse
from django.utils import timezone
from django.db.models.query import QuerySet

from rest_framework.test import APIClient
from rest_framework.response import Response

from .models import Outflow, Inflow


EXCLUDED_KEYS = ['creation_date', 'last_modification', 'id']


def extract_and_clean_dict(response: Response, keys_to_remove: list) -> dict:
    """
    Extracts the first item from the API response data and removes specified keys from it.

    Args:
        response (Response): The API response containing the data.
        keys_to_remove (list): A list of keys that should be removed from the extracted dictionary.

    Returns:
        dict: A cleaned dictionary with the specified keys removed.
    """
    assert isinstance(response.data[0], dict)
    data: dict = response.data[0]
    return {k: v for k, v in data.items() if k not in keys_to_remove}


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

    def test_get_request_empty_DB(self) -> None:
        response: Response = self.api_client.get(self.url)
        assert response.status_code == 200
        assert response.data == []

    def test_get_request_one_record_DB(self) -> None:
        Outflow.objects.create(**self.example_fixture)
        response: Response = self.api_client.get(self.url)
        cleaned_result: dict = extract_and_clean_dict(response, EXCLUDED_KEYS)
        assert cleaned_result == self.example_fixture

    def test_get_request_one_record_DB_current_date(self) -> None:
        Outflow.objects.create(**self.example_fixture)
        params = {
            'year': timezone.now().year,
            'month': timezone.now().month
        }
        response: Response = self.api_client.get(self.url, params)
        cleaned_result: dict = extract_and_clean_dict(response, EXCLUDED_KEYS)
        assert cleaned_result == self.example_fixture

    def test_get_request_one_record_DB_not_current(self) -> None:
        Outflow.objects.create(**self.example_fixture)
        params = {
            'year': timezone.now().year,
            'month': 1
        }
        response: Response = self.api_client.get(self.url, params)
        assert response.data == []

    def test_post_request(self) -> None:
        self.api_client.post(self.url, self.example_fixture)
        queryset: QuerySet = Outflow.objects.all()
        assert len(queryset) == 1


@pytest.mark.django_db
class TestOneInflowsView:
    url: str = reverse('inflows')
    example_fixture: dict = {
        'title': 'Mario in DB',
        'value': '123.45',
        'date': datetime.now().strftime('%Y-%m-%d'),
        'notes': ''
    }
    api_client: APIClient = APIClient()

    def test_get_request_empty_DB(self) -> None:
        response: Response = self.api_client.get(self.url)
        assert response.status_code == 200
        assert response.data == []

    def test_get_request_one_record_DB(self) -> None:
        Inflow.objects.create(**self.example_fixture)
        response: Response = self.api_client.get(self.url)
        cleaned_result: dict = extract_and_clean_dict(response, EXCLUDED_KEYS)
        assert cleaned_result == self.example_fixture

    def test_get_request_one_record_DB_current_date(self) -> None:
        Inflow.objects.create(**self.example_fixture)
        params = {
            'year': timezone.now().year,
            'month': timezone.now().month
        }
        response: Response = self.api_client.get(self.url, params)
        cleaned_result: dict = extract_and_clean_dict(response, EXCLUDED_KEYS)
        assert cleaned_result == self.example_fixture

    def test_get_request_one_record_DB_not_current(self) -> None:
        Inflow.objects.create(**self.example_fixture)
        params = {
            'year': timezone.now().year,
            'month': 1
        }
        response: Response = self.api_client.get(self.url, params)
        assert response.data == []

    def test_post_request(self) -> None:
        self.api_client.post(self.url, self.example_fixture)
        queryset: QuerySet[Inflow] = Inflow.objects.all()
        assert len(queryset) == 1


