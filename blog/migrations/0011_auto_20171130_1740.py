# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 17:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20171122_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
