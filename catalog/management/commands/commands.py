from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        data = [{'name': 'Бакалея', 'description': 'список товаров в этой категории'},
                 {'name': 'Выпечка', 'description': 'список свежей выпечки'},
                 {'name': 'Готовые блюда', 'description': 'Список свежих готовых блюд'},]

        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1")
            cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1")

        new_data = []
        for item in data:
            new_data.append(
                Category(**item)
            )
        Category.objects.bulk_create(new_data)

