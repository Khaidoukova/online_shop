from django.db import models

NULLABLE = {'blank': True, 'null': True}
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.CharField(max_length=100, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    creation_date = models.DateTimeField(verbose_name='дата создания')
    change_date = models.DateTimeField(verbose_name='дата последнего изменения')


    def __str__(self):
        return f'{self.name}, {self.category}, {self.price} rub'

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')


    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ('name',)

