# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0002_auto_20170623_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='last_update',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='channel',
            name='last_update',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
