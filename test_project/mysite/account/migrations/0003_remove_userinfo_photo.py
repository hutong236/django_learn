# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-06-22 16:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_userinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='photo',
        ),
    ]