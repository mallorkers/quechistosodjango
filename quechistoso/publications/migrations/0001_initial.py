# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('body', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Moderate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_id', models.CharField(max_length=40, blank=True)),
                ('date_moderation', models.DateTimeField(auto_now=True)),
                ('vote', models.IntegerField(choices=[(0, b'Aprobado'), (1, b'Rechazado'), (2, b'Muy Visto')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, b'Publicado'), (1, b'Moderando'), (3, b'Eliminado')])),
                ('body', models.TextField()),
                ('session_id', models.CharField(max_length=32, blank=True)),
            ],
            options={
                'ordering': ('date_time',),
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
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nick', models.CharField(max_length=50)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='publication',
            name='owner',
            field=models.ForeignKey(to='publications.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publication',
            name='tags',
            field=models.ManyToManyField(to='publications.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='moderate',
            name='publication',
            field=models.ForeignKey(to='publications.Publication'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='moderate',
            name='user_profile',
            field=models.ForeignKey(blank=True, to='publications.UserProfile', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='publication',
            field=models.ForeignKey(to='publications.Publication'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user_profile',
            field=models.ForeignKey(to='publications.UserProfile'),
            preserve_default=True,
        ),
    ]
