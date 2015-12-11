# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bar',
            name='genre',
        ),
        migrations.AddField(
            model_name='bar',
            name='fancy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bar',
            name='has_sports',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bar',
            name='is_dive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='fancy',
            field=models.BooleanField(default=False),
        ),
    ]
