# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0004_auto_20150523_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moderate',
            name='vote',
            field=models.IntegerField(choices=[(0, 'Aprobado'), (1, 'Rechazado'), (2, 'Muy Visto')]),
        ),
        migrations.AlterField(
            model_name='publication',
            name='status',
            field=models.IntegerField(choices=[(0, 'Publicado'), (1, 'Moderando'), (3, 'Eliminado')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='genders',
            field=models.CharField(max_length=2, choices=[('NE', 'No Especificado'), ('M', 'Masculino'), ('F', 'Femenino')], default='NE'),
        ),
    ]
