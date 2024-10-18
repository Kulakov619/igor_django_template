import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, db_column='created')
    updated = models.DateTimeField(auto_now=True, db_column='updated')

    class Meta:
        abstract = True


class Role(models.TextChoices):
    TEACHER = 'teacher', _('Teacher')
    STUDENT = 'student', _('Student')


class User(AbstractUser):
    third_name = models.CharField("отчество", max_length=500, blank=True)
    role = models.TextField(_('Role'), choices=Role.choices)

    class Meta:
        verbose_name = _('пользователь')
        verbose_name_plural = _('пользователи')
        ordering = ['last_name']


class Order(TimeStampedMixin):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column='user_id',
        verbose_name=_('user')
    )
    book = models.ForeignKey(
        'Book',
        on_delete=models.CASCADE,
        db_column='book_id',
        verbose_name=_('book')
    )
    date_start = models.DateField(_('date start'))
    date_end = models.DateField(_('date end'))

    class Meta:
        verbose_name = _('заказ')
        verbose_name_plural = _('заказы')


class Book(TimeStampedMixin):
    name = models.CharField("название", max_length=500)
    autor = models.ForeignKey(
        'Autor',
        on_delete=models.CASCADE,
        db_column='autor_id',
        verbose_name=_('autor')
    )

    class Meta:
        verbose_name = _('книга')
        verbose_name_plural = _('книги')


class Autor(TimeStampedMixin):
    name = models.CharField("имя", max_length=500)
    surname = models.CharField("фамилия", max_length=500)
    third_name = models.CharField("отчество", max_length=500, blank=True)

    class Meta:
        verbose_name = _('автор')
        verbose_name_plural = _('авторы')