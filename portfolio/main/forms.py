import re
from django import forms
from .models import Project
from captcha.fields import CaptchaField


class ProjectForm(forms.ModelForm):
    captcha = CaptchaField()

    def clean_name(self):
        name = self.cleaned_data['name']
        if re.match(r'\d', name):
            raise ValueError('Заголовок не должен начинаться с цифр')
        return name

    class Meta:
        model = Project
        # fields = '__all__'
        fields = ['name', 'description', 'is_published', 'category']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
