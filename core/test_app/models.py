from django.db import models


class TestModel(models.Model):
    id = models.IntegerField(
        'id', unique=True, primary_key=True, editable=False)
    name = models.CharField('name', max_length=20)
    text = models.TextField('text')
    img = models.ImageField('image', upload_to='images/', null=True, blank=True)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.name

