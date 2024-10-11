from django.views.generic import TemplateView, CreateView
from .models import TestModel
from .forms import TestModelForm


class TestPage(TemplateView):
    template_name = 'test_app/test_page.html'


class TestPageNew(TemplateView):
    template_name = 'test_app/test_page_1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = TestModel.objects.all().order_by('name')
        context['posts'] = posts
        return context


class CreatePost(CreateView):
    template_name = 'test_app/form.html'
    form_class = TestModelForm

