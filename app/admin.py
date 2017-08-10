# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Item

class ItemAdmin(admin.ModelAdmin):
    search_fields = ('name', 'brand', 'iid')
    list_filter = ('brand',)
    list_per_page = 10

    def image_tag(self, obj):
        return u'<img src="%s" weight=50 height=50/>' % obj.imgUrls.split('\n')[0]
    image_tag.short_description = '主图'
    image_tag.allow_tags = True


    def source_tag(self, obj):
        return u'<a href="%s" target="_blank"/>官网链接</a>' % obj.itemUrl
    source_tag.short_description = '官网链接'
    source_tag.allow_tags = True

    list_display = ('image_tag', 'source_tag', 'iid', 'name', 'brand', 'category', 'weight', 'price')


# Register your models here.
admin.site.register(Item, ItemAdmin)