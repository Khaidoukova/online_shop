from django.contrib import admin

from catalog.models import Product, Category, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'is_active')
    list_filter = ('category', 'is_active',)
    search_fields = ('name', 'description', 'is_active',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version', 'version_name', 'is_active')
    list_display_links = ('version', 'version_name',)
    list_editable = ('is_active',)
