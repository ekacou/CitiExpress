# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-02 17:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20190401_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='business',
        ),
        migrations.DeleteModel(
            name='Business',
        ),
    ]