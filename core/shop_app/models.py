from django.db import models


class IdMixin(models.Model):
    id = models.IntegerField(primary_key=True, editable=False, unique=True)

    class Meta:
        abstract = True


class Category(IdMixin):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'


class Product(IdMixin):
    name = models.CharField('name', max_length=100)
    price = models.DecimalField('price', max_digits=10, decimal_places=2)
    description = models.TextField('description', blank=True, null=True)
    imageUrl = models.ImageField('imageUrl', upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'product'
        verbose_name_plural = 'products'

