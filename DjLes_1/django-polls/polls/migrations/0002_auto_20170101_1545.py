# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-01 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='Запитання',
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date publishing'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
