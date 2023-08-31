from django.db import models
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(**NULLABLE, verbose_name='описание')

    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.CharField(max_length=100, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    change_date = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='автор', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='опубликован')

    def __str__(self):
        return f'{self.name}, {self.category}, {self.price} руб/кг'

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        permissions = [
            (
                "set_active_status",
                "Can activate product"
            )
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version = models.CharField(max_length=20, verbose_name='номер версии')
    version_name = models.CharField(max_length=20, verbose_name='название версии')
    is_active = models.BooleanField(default=False, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.version_name}, {self.version}'

    class Meta:
        verbose_name = "версия"
        verbose_name_plural = "версии"

def toggle_activity(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    if product_item.is_active:
        product_item.is_active = False
    else:
        product_item.is_active = True

    product_item.save()

    return redirect(reverse('home'))