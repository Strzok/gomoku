# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-10-25 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20181025_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coord_o',
            name='coord_ox',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='coord_o',
            name='coord_oy',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='coord_x',
            name='coord_xx',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='coord_x',
            name='coord_xy',
            field=models.CharField(max_length=200),
        ),
    ]
