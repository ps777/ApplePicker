# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-12 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(help_text='why me'),
        ),
    ]
