# myapp/management/commands/populate_data.py
from django.core.management.base import BaseCommand
from store.fak.faker import MyModelFactory

class Command(BaseCommand):
    help = 'Populate database with test data'

    def handle(self, *args, **kwargs):
        for _ in range(10):  # Create 10 products
            MyModelFactory()
        self.stdout.write(self.style.SUCCESS('Successfully populated database with test data'))
