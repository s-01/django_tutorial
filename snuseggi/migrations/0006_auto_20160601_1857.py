# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snuseggi', '0005_auto_20160601_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='restuarant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snuseggi.Restaurant'),
        ),
    ]