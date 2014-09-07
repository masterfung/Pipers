# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_event_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_date',
        ),
        migrations.AddField(
            model_name='event',
            name='event_url',
            field=models.URLField(default='www.test.com'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='venue_name',
            field=models.CharField(default='test', max_length=200, blank=True),
            preserve_default=False,
        ),
    ]
