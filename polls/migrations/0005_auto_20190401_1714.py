# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-01 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20190401_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='employee_username',
        ),
        migrations.AddField(
            model_name='employee',
            name='username',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
