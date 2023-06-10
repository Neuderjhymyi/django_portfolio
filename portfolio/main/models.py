from django.db import models
from django.urls import reverse_lazy, reverse


class Project(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя проекта')
    description = models.TextField(blank=True, verbose_name='Описание')
    link = models.URLField(default=None, null=True, verbose_name='ссылка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    photo = models.ImageField(null=True, upload_to='media/%Y/%m/%d', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def get_absolute_url(self):
        # return reverse('View_project', args=[str(self.pk)])
        return reverse_lazy('View_project', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse_lazy('Category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
