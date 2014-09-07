# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='user_event_status',
            field=models.CharField(default=b'Not Attending', max_length=15, choices=[(b'Not Attending', b'Not Attending'), (b'Attending', b'Attending')]),
            preserve_default=True,
        ),
    ]
