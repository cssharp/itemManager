# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='iid',
            field=models.CharField(max_length=1000, verbose_name='\u4ea7\u54c1\u578b\u53f7'),
        ),
        migrations.AlterField(
            model_name='item',
            name='imgUrls',
            field=models.CharField(max_length=2000, verbose_name='\u56fe\u7247\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=1000, verbose_name='\u5b9d\u8d1d\u540d\u79f0\uff08\u82f1\uff09'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(verbose_name='\u6d77\u5916\u4ef7\u683c\uff08\u7f8e\u5143\uff09'),
        ),
        migrations.AlterField(
            model_name='item',
            name='sizes',
            field=models.CharField(max_length=2000, verbose_name='\u53ef\u9009\u5c3a\u7801'),
        ),
    ]
