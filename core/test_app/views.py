from django.views.generic import TemplateView


class TestPage(TemplateView):
    template_name = 'test_app/test_page.html'


class TestPageNew(TemplateView):
    template_name = 'test_app/test_page_1.html'