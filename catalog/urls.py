from django.contrib import admin
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, add_product, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('add_product/', add_product, name='add_product'),
]
