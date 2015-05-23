# -*- encoding: utf-8 -*-
from apps.publications.models import Tag
__author__ = 'broker'

def categories_processor(request):
    ctx = dict()
    ctx["all_tags"] = Tag.objects.all()
    return ctx