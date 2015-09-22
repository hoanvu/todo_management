# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_remove_todo_datecreated'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 21, 13, 51, 59, 744000, tzinfo=utc), verbose_name=b'Created date', auto_now_add=True),
            preserve_default=False,
        ),
    ]
