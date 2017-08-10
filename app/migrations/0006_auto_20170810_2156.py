# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170810_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sizes',
            field=models.TextField(verbose_name='\u53ef\u9009\u5c3a\u7801'),
        ),
    ]
