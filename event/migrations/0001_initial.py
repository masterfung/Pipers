# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_id', models.CharField(max_length=15, unique=True, null=True)),
                ('event_name', models.CharField(max_length=100, blank=True)),
                ('event_location', models.CharField(max_length=50, blank=True)),
                ('event_address', models.CharField(max_length=400, blank=True)),
                ('event_address2', models.CharField(max_length=400, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('city', models.CharField(max_length=50, blank=True)),
                ('event_date', models.DateTimeField()),
                ('event_start', models.DateTimeField()),
                ('event_end', models.DateTimeField()),
                ('state', models.CharField(max_length=20, blank=True)),
                ('zip', models.CharField(max_length=20, blank=True)),
                ('country', models.CharField(max_length=30, blank=True)),
                ('lat', models.FloatField(max_length=30, null=True, blank=True)),
                ('lon', models.FloatField(max_length=30, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
