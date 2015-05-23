# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0003_auto_20150523_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='owner',
            field=models.ForeignKey(blank=True, to='publications.UserProfile', null=True),
        ),
    ]
