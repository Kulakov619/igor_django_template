from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from datetime import date
from openpyxl import Workbook, load_workbook
from .models import UploadFile
from .forms import UploadForm


# Create your views here.
@method_decorator(login_required, name='dispatch')
class ImportView(CreateView):
    model = UploadFile
    form_class = UploadForm
    success_url = '/'
    template_name = 'import_app/import.html'

    def form_valid(self, form, **kwargs):
        o = form.save(commit=False)
        o.save()
        filename = o.file
        wb = load_workbook(filename=filename)
        sheet = wb.active
        a = sheet.cell(row=9, column=1).value
        o.is_ok = True
        return super(ImportView, self).form_valid(form)
