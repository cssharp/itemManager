# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20170810_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='cnPrice',
            field=models.FloatField(null=True, verbose_name='\u4ee3\u8d2d\u4ef7\u683c', blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(null=True, verbose_name='\u6d77\u5916\u4ef7\u683c\uff08\u7f8e\u5143\uff09', blank=True),
        ),
    ]
