# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0006_auto_20150829_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=100),
            preserve_default=False,
        ),
    ]
