# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.template import defaultfilters


class Tag(models.Model):
    u""" Etiquetas de las publicaciones """

    tag = models.CharField(max_length=30)
    slug = models.SlugField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.tag)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.tag


class UserProfile(models.Model):

    GENDERS = (
        ("NE", "No Especificado"),
        ("M", "Masculino"),
        ("F", "Femenino"),
    )

    def url(self, filename):
        ruta = "MultimediaData/users/%s/%s"%(self.user.username,filename)
        return ruta

    user = models.OneToOneField(User)
    nick = models.CharField(max_length=50, null=True, blank=True)
    genders = models.CharField(choices=GENDERS, default="NE", max_length=2)
    birthday = models.DateField('Fecha de nacimiento', null=True, blank=True)
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
    owner = models.ForeignKey(UserProfile, blank=True, null=True)
    session_id = models.CharField(max_length=32, blank=True)
    tags = models.ManyToManyField(Tag)
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    @property
    def number_comments(self):
        return self.comment_set.all().count()

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




