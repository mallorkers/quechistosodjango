# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Publicacion, Comment, Moderado, Tag


class TagsAdmin(admin.ModelAdmin):
    pass

class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('id','status','fecha','owner')
    list_filter = ('fecha','status')
    search_fields = ('id','owner')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','usuario','publicacion','fecha')


class ModeradoAdmin(admin.ModelAdmin):
    list_display = ('publicacion','voto','usuario','session_id')
    list_filter = ('publicacion',)

admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Moderado, ModeradoAdmin)
admin.site.register(Tag, TagsAdmin)