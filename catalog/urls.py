from django.contrib import admin
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductCreateView, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_form'),
]
