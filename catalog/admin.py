from django.contrib import admin

from catalog.models import Product, Category, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'status')
    list_filter = ('category', 'status',)
    search_fields = ('name', 'description', 'status',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version', 'version_name', 'is_active')
    list_display_links = ('version', 'version_name',)
    list_editable = ('is_active',)
