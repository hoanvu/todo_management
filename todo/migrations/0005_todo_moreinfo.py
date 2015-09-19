# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20150915_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='moreinfo',
            field=models.CharField(max_length=400, blank=True),
        ),
    ]
