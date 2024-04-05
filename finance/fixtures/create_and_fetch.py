import json
from faker import Faker
from random import randint, choice
from django.contrib.auth.models import User
from finance.models import Currency
"""
This scrypt creates a fixture with fake data that will be dumped do DB

It starts with 1 January 2023 and creates data up to today.

It creates between 25 and 50 outcomes and between 2 and 5 incomes

At first of the month there is salary which is the biggest income
then it adds 1 to 4 side incomes

  [{
    "model": "finance.oneio",
    "fields": {
      "is_outcome": false,
      "title": "This month income",
      "value": 100,
      "date": "__CURRENT_MONTH__",
      "owner": 1,
      "currency": 1,
      "future": true,
      "cash_tag": null,
      "company": null,
      "notes": "This is a sample income",
      "creation_date": "2023-02-01T00:00:00Z",
      "last_modification": "2023-02-01T00:00:00Z"
    }
  },]
"""


def create_and_fetch() -> None:
    User.objects.create()
    Currency.objects.create()



if __name__ == '__main__':
    create_and_fetch()