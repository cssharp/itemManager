# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170810_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='brand',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u54c1\u724c', blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='iid',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u4ea7\u54c1\u578b\u53f7', blank=True),
        ),
    ]
