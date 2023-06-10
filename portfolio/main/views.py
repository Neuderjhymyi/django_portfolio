from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import ListView, DetailView, CreateView
# from django.contrib import messages
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login, logout
from .models import Project, Category
from .forms import ProjectForm


def main_home(request):
    # news = Project.objects.all()
    # categories = Category.objects.all()
    context = {
        'title': 'Главная страница',
    }
    return render(request, 'main/home_project.html', context=context)


def my_contacts(request):
    context = {
        'title': 'Мои контакты',
    }
    return render(request, 'main/my_contacts.html', context=context)


def about_me(request):
    context = {
        'title': 'Обо мне',
    }
    return render(request, 'main/about_me.html', context=context)


class HomeProject(ListView):
    model = Project
    context_object_name = 'project'
    template_name = 'main/home_project_list.html'
    extra_context = {'title': 'Проекты'}
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Project.objects.filter(is_published=True).select_related('category')


class ProjectByCategory(ListView):
    model = Project
    template_name = 'main/project_list.html'
    context_object_name = 'project_by_category'
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id']).title
        return context

    def get_queryset(self):
        return Project.objects.filter(category_id=self.kwargs['category_id'],
                                      is_published=True).select_related('category')


class ViewProject(DetailView):
    model = Project
    template_name = 'main/project_detail.html'
    context_object_name = 'project_item'


class AddProject(CreateView):
    form_class = ProjectForm
    template_name = 'main/add_project.html'
    login_url = '/admin/'

