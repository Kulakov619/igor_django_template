from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import TestModel
from .forms import TestModelForm
from django.contrib.auth.hashers import make_password


class TestPage(TemplateView):
    template_name = 'test_app/test_page.html'


class TestPageNew(TemplateView):
    template_name = 'test_app/test_page_1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(make_password('12345'))
        posts = TestModel.objects.all().order_by('name')
        context['posts'] = posts
        return context


class CreatePost(CreateView):
    template_name = 'test_app/form.html'
    form_class = TestModelForm
    success_url = '/'


class UpdatePost(UpdateView):
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = 'test_app/form.html'
    form_class = TestModelForm
    model = TestModel
    success_url = '/'


class DeletePost(DeleteView):
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = 'test_app/delete.html'
    model = TestModel
    success_url = '/'


class DetailPost(DetailView):
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = 'test_app/detail.html'
    model = TestModel


class ListPost(ListView):
    template_name = 'test_app/list.html'
    model = TestModel


