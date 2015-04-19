from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # profiel_picture = models.ImageField(upload_to=url)

    def __str__(self):
        return self.user.username
