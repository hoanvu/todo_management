# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_todo_moreinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='dateCreated',
        ),
    ]
