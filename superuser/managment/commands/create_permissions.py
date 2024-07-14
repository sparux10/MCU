# myapp/management/commands/create_permissions.py
from django.core.management.base import BaseCommand
from superuser.models import Permission

class Command(BaseCommand):
    help = 'Create initial permissions'

    def handle(self, *args, **kwargs):
        permissions = [
            {'name': 'Full administrative access', 'code': 'full_admin'},
            {'name': 'Can manage products', 'code': 'product_admin'},
            {'name': 'Can edit content', 'code': 'content_editor'},
        ]

        for perm in permissions:
            Permission.objects.get_or_create(name=perm['name'], code=perm['code'])

        self.stdout.write(self.style.SUCCESS('Successfully created permissions'))
