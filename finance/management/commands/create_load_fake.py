import os
import subprocess

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from finance.fixtures.create_and_load import create_fake_json


class Command(BaseCommand):
    help = 'Create a fixture and loads it to DB - Do not use in production'

    def handle(self, *args, **options):
        file_path = 'finance/fixtures/cash_flow_from_31_1_2023_to_now.json'
        if os.path.exists(file_path):
            with open(file_path, 'w'):
                pass

        fake_json = create_fake_json()
        with open(file_path, 'w') as file:
            file.write(fake_json)

        try:
            subprocess.run(['python', 'manage.py', 'loaddata', file_path], check=True)
            self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))
        except subprocess.CalledProcessError as e:
            self.stdout.write(self.style.ERROR(f'Error loading fixture: {e}'))
