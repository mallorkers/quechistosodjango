# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):

      tag = models.CharField(max_length=30)

      def __str__(self):
          return self.tag


class UserProfile(models.Model):

    def url(self, filename):
        ruta = "MultimediaData/users/%s/%s"%(self.user.username,filename)
        return ruta

    user = models.OneToOneField(User)
    nick = models.CharField(max_length=50)
    # profiel_picture = models.ImageField(upload_to=url)

    def __str__(self):
        return self.user.username

    @property
    def username(self):
        return self.user.username


class Publication(models.Model):

    STATUS = (
        (0, "Publicado"),
        (1, "Moderando"),
        (3, "Eliminado")
    )

    date_time = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS)
    body = models.TextField()
    owner = models.ForeignKey(UserProfile)
    session_id = models.CharField(max_length=32, blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        ordering = ('date_time',)





class Moderate(models.Model):

    VOTES = (
        (0, "Aprobado"),
        (1, "Rechazado"),
        (2, "Muy Visto")
    )
    user_profile = models.ForeignKey(UserProfile, blank=True, null=True)
    publication = models.ForeignKey(Publication)
    session_id = models.CharField(max_length=40, blank=True)
    date_moderation = models.DateTimeField(auto_now=True)
    vote = models.IntegerField(choices=VOTES)

    def __str__(self):
        return "%s" % self.id


class Comment(models.Model):

    date_time = models.DateTimeField(auto_now=True)
    body = models.TextField()
    publication = models.ForeignKey(Publication)
    user_profile = models.ForeignKey(UserProfile)

    def __str__(self):
        return "%s" % self.id




