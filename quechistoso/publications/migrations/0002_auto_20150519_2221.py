# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='likes',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publication',
            name='views',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='genders',
            field=models.CharField(default=b'NE', max_length=2, choices=[(b'NE', b'No Especificado'), (b'M', b'Masculino'), (b'F', b'Femenino')]),
            preserve_default=True,
        ),
    ]
