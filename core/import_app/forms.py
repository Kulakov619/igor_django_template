from django.forms import ModelForm
from .models import UploadFile


class UploadForm(ModelForm):
    class Meta:
        model = UploadFile
        fields = ['name', 'file']