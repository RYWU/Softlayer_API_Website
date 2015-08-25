# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0002_auto_20150817_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 18, 3, 30, 4, 525552, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
