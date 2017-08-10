# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170810_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='imgUrls',
            field=models.TextField(null=True, verbose_name='\u56fe\u7247\u5730\u5740', blank=True),
        ),
    ]
