from django.db import models
from django.conf import settings


class UserAbout(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    third_name = models.CharField(max_length=100)

