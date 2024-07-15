# Generated by Django 5.0.7 on 2024-07-15 21:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OCApp', '0002_alter_cartproduct_color_size_and_more'),
        ('store', '0008_myuser_alter_category_user_alter_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.myuser'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.myuser'),
        ),
    ]
