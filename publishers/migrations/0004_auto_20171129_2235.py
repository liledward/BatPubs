# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-29 22:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publishers', '0003_auto_20171129_2234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publisher',
            old_name='url',
            new_name='website_address',
        ),
    ]
