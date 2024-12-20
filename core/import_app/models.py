from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator


class UploadFile(models.Model):
    id = models.IntegerField(
        'id', unique=True, primary_key=True, editable=False)
    name = models.CharField("краткое описание действия", max_length=500)
    file = models.FileField("выберите файл xlsx", upload_to='upload/',
                            validators=[FileExtensionValidator(['xlsx'])])
    is_ok = models.BooleanField("успешная загрузка", default=False)
    log = models.TextField("лог")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'лог загрузки постов'
        verbose_name_plural = 'логи загрузки постов'
        ordering = ['-created_at']