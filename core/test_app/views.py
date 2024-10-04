from django.views.generic import TemplateView
from .models import TestModel


class TestPage(TemplateView):
    template_name = 'test_app/test_page.html'


class TestPageNew(TemplateView):
    template_name = 'test_app/test_page_1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = TestModel.objects.all().order_by('name')
        context['posts'] = posts
        return context

