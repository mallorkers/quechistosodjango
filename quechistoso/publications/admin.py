# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Publication, Comment, Moderate, Tag


# Inline
class PublicationInline(admin.TabularInline):
    model = Publication
    extra = 1


class ModerateInline(admin.TabularInline):
    model = Moderate
    extra = 1


class CommentsInline(admin.TabularInline):
    model = Comment
    extra = 1

class TagsAdmin(admin.ModelAdmin):
    pass


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('id','status','date_time','owner')
    list_filter = ('date_time','status')
    search_fields = ('id','owner')

    inlines = [ModerateInline, CommentsInline]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','user_profile','publication','date_time')


class ModerateAdmin(admin.ModelAdmin):
    list_display = ('publication','vote','user_profile','session_id')
    list_filter = ('publication',)






admin.site.register(Publication, PublicationAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Moderate, ModerateAdmin)
admin.site.register(Tag, TagsAdmin)