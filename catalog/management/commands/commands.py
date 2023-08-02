from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        data = [{'name': 'Бакалея', 'description': 'список товаров в этой категории'},
                 {'name': 'Выпечка', 'description': 'список свежей выпечки'},
                 {'name': 'Готовые блюда', 'description': 'Список свежих готовых блюд'},]

        new_data = []
        for item in data:
            new_data.append(
                Category(**item)
            )
        Category.objects.bulk_create(new_data)

