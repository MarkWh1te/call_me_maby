# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-16 04:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_remove_menus_query'),
        ('explorer', '0006_query_activate'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.Menus'),
        ),
    ]
