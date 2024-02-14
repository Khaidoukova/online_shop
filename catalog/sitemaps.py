from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Product

class ProductSitemap(Sitemap):

    changefreq = 'daily'
    priority = 0.9
    limit = 50  # Количество объектов на одной странице
    protocol = 'https'  # Протокол (можно использовать 'http' или 'https')

    def items(self):
        return Product.objects.all()

    def location(self, obj):
        view_name = 'catalog:product_detail'
        kwargs = {'pk': obj.id}
        return reverse(view_name, kwargs=kwargs)



