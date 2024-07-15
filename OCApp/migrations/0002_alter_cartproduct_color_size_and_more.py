# Generated by Django 5.0.7 on 2024-07-15 21:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OCApp', '0001_initial'),
        ('store', '0006_remove_colorsize_color_remove_colorsize_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='color_size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.productcolorsize'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='color_size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.productcolorsize'),
        ),
    ]
