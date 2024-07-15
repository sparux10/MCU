# Generated by Django 5.0.7 on 2024-07-15 21:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_category_id_product_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colorsize',
            name='color',
        ),
        migrations.RemoveField(
            model_name='colorsize',
            name='size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='color_sizes',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='categoury_img',
            new_name='category_img',
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='store.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ProductColorSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_colors_sizes', to='store.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_colors_sizes', to='store.product')),
                ('size', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_colors_sizes', to='store.size')),
            ],
        ),
    ]