from django.contrib import admin
from .models import UploadFile


@admin.register(UploadFile)
class TestModelAdmin(admin.ModelAdmin):
    list_display = ("name", "is_ok")
    search_fields = ("name", "is_ok")

