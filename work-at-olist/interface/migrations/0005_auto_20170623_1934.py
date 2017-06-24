# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0004_auto_20170623_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='last_update',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='last_update',
        ),
    ]
