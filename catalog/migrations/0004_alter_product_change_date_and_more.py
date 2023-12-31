# Generated by Django 4.2.3 on 2023-08-10 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_category_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='change_date',
            field=models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата создания'),
        ),
    ]
