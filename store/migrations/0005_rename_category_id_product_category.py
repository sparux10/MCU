# Generated by Django 5.0.7 on 2024-07-12 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_product_colors_remove_product_sizes_colorsize_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category_id',
            new_name='category',
        ),
    ]