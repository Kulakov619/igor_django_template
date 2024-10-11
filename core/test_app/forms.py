from django.forms import ModelForm
from .models import TestModel


class TestModelForm(ModelForm):
    class Meta:
        model = TestModel
        fields = ['id', 'name', 'text', 'img']

