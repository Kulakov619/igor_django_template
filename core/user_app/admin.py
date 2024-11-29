from django.contrib import admin
from .models import UserAbout


@admin.register(UserAbout)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user",)

