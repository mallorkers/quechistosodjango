# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0005_auto_20150827_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(verbose_name='Fecha de nacimiento', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nick',
            field=models.CharField(null=True, max_length=50, blank=True),
        ),
    ]
