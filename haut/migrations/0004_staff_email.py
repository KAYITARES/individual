# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-17 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haut', '0003_auto_20190417_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]