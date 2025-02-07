from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Category, Product


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name", "price")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


