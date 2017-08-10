# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Item

# Create your views here.

def xx():
    items = Item.objects.all()
    for x in items:
        print x

if __name__ == '__main__':
    xx()