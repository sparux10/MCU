# Generated by Django 5.0.6 on 2024-07-06 19:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0005_remove_myuser_role_remove_role_code_role_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='role',
        ),
        migrations.AddField(
            model_name='role',
            name='users',
            field=models.ManyToManyField(related_name='role', to=settings.AUTH_USER_MODEL),
        ),
    ]
