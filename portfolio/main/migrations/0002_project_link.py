# Generated by Django 4.2.1 on 2023-05-17 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(default=None, verbose_name='ссылка'),
        ),
    ]