from django.contrib import admin
from django.urls import path
from django.views.decorators.cache import cache_page

from .views import HomeProject, ProjectByCategory, ViewProject, AddProject, about_me, main_home, my_contacts


urlpatterns = [
    path('', cache_page(2)(main_home), name='main_home'),
    path('main/', cache_page(2)(HomeProject.as_view()), name='MainProject'),
    path('category/<int:category_id>', ProjectByCategory.as_view(), name='Category'),
    path('main/<int:pk>', ViewProject.as_view(), name='View_project'),
    path('project/add_project', AddProject.as_view(), name='Add_project'),
    path('about_me/', about_me, name='about_me'),
    path('my_contacts/', my_contacts, name='my_contacts'),
    # path('register/', register, name='Register'),
    # path('login/', user_login, name='Login'),
    # path('logout/', user_logout, name='Logout'),
]

