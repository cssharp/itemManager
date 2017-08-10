# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Item(models.Model):
    class Meta:
        verbose_name = '宝贝' #提供了一个更容易让人阅读的名称
        verbose_name_plural = '宝贝列表' #复数形式
    id = models.AutoField(primary_key=True)
    brand = models.CharField("品牌", max_length=1000, null=False, blank=False)
    iid = models.CharField("产品型号", max_length=1000, null=False, blank=False)
    name = models.CharField("宝贝名称（英）", max_length=1000, null=True, blank=True)
    imgUrls = models.TextField("图片地址", null=True, blank=True)
    category = models.CharField("分类", max_length=1000, null=True, blank=True)
    weight = models.CharField("重量（磅）", max_length=1000, null=True, blank=True)
    sizes = models.TextField("可选尺码")
    gender = models.CharField("性别", max_length=1000, null=True, blank=True)
    itemUrl = models.CharField("官网地址", max_length=1000, null=True, blank=True)
    price = models.FloatField("海外价格（美元）", null=True, blank=True)
    cnPrice = models.FloatField("代购价格", null=True, blank=True)
    feature = models.TextField("描述（英）", null=True, blank=True)
    featureTrans = models.TextField("描述（翻译）", null=True, blank=True)
