from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Project, Category


class ProjectAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Project
        fields = '__all__'


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'description', 'created_at',
                    'updated_at', 'get_photo', 'photo', 'is_published', 'link')
    list_display_links = ('id',)
    search_fields = ('name', 'description')
    list_filter = ('id', 'name')
    list_editable = ('category', 'name', 'description', 'photo', 'is_published', 'link')
    fields = ('name', 'description', 'photo', 'is_published', 'category',  'link')
    readonly_fields = ('get_photo', 'created_at', 'updated_at')
    form = ProjectAdminForm

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'Фото нет'

    get_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Страница администратора'
admin.site.site_header = 'Страница администратора'