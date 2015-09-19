# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todo'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, b'In Progress'), (1, b'Pending'), (2, b'Done'), (3, b'Cancelled')]),
        ),
        migrations.AlterField(
            model_name='todo',
            name='dateCreated',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Date created'),
        ),
    ]
