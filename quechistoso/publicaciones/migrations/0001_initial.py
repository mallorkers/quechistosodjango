# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('body', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Moderado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_id', models.CharField(max_length=40)),
                ('fecha_moderacion', models.DateTimeField(auto_now=True)),
                ('voto', models.IntegerField(choices=[(0, b'Aprobado'), (1, b'Rechazado'), (2, b'Muy Visto')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, b'Publicado'), (1, b'Moderando'), (3, b'Eliminado')])),
                ('body', models.TextField()),
                ('owner', models.OneToOneField(to='usuarios.UserProfile')),
            ],
            options={
                'ordering': ('fecha',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='tags',
            field=models.ManyToManyField(to='publicaciones.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='moderado',
            name='publicacion',
            field=models.ForeignKey(to='publicaciones.Publicacion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='moderado',
            name='usuario',
            field=models.ForeignKey(blank=True, to='usuarios.UserProfile', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='publicacion',
            field=models.ForeignKey(to='publicaciones.Publicacion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='usuario',
            field=models.ForeignKey(to='usuarios.UserProfile'),
            preserve_default=True,
        ),
    ]
