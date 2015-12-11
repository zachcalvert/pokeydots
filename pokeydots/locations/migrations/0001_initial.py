# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=75, null=True, blank=True)),
                ('genre', models.CharField(help_text=b'What kind of bar is this?', max_length=30, choices=[(b'swanky', b'Swanky'), (b'divey', b'Dive')])),
                ('has_games', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=75, null=True, blank=True)),
                ('genre', models.CharField(help_text=b'What kind of restaurant is this?', max_length=30, choices=[(b'mexican', b'Mexican'), (b'sushi', b'Sushi'), (b'thai', b'Thai'), (b'american', b'American')])),
                ('has_liquor', models.BooleanField(default=False)),
                ('neighborhood', models.ForeignKey(to='locations.Neighborhood')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='bar',
            name='neighborhood',
            field=models.ForeignKey(to='locations.Neighborhood'),
        ),
    ]
