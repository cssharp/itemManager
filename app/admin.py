# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'weight', 'price')
    search_fields = ('name', 'brand')

# Register your models here.
admin.site.register(Item, ItemAdmin)