# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-06-09 14:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index_monitor_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='responsedata',
            old_name='total_number',
            new_name='num_found',
        ),
    ]