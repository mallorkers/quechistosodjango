# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_auto_20150519_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='owner',
            field=models.ForeignKey(to='publications.UserProfile', null=True),
        ),
    ]
