# -*- encoding: utf-8 -*-
from django.db import models
from usuarios.models import UserProfile


class Tag(models.Model):

      tag = models.CharField(max_length=30)

      def __str__(self):
          return self.tag


class Publicacion(models.Model):

    STATUS = (
        (0, "Publicado"),
        (1, "Moderando"),
        (3, "Eliminado")
    )

    fecha = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS)
    body = models.TextField()
    owner = models.OneToOneField(UserProfile)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        ordering = ('fecha',)

class Moderado(models.Model):

    VOTOS = (
        (0, "Aprobado"),
        (1, "Rechazado"),
        (2, "Muy Visto")
    )
    usuario = models.ForeignKey(UserProfile, blank=True, null=True)
    publicacion = models.ForeignKey(Publicacion)
    session_id = models.CharField(max_length=40, blank=True)
    fecha_moderacion = models.DateTimeField(auto_now=True)
    voto = models.IntegerField(choices=VOTOS)

    def __str__(self):
        return "%s" % self.id

class Comment(models.Model):

    fecha = models.DateTimeField(auto_now=True)
    body = models.TextField()
    publicacion = models.ForeignKey(Publicacion)
    usuario = models.ForeignKey(UserProfile)

    def __str__(self):
        return "%s" % self.id

