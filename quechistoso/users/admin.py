from django.contrib import admin
from users.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','username','email')

    def username(self, object):
        return object.user.username

    def email(self, object):
        return object.user.email
admin.site.register(UserProfile, UserProfileAdmin)