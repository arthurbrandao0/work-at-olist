# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0003_auto_20170623_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='last_update',
            field=models.DateTimeField(null=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='channel',
            name='last_update',
            field=models.DateTimeField(null=True, default=django.utils.timezone.now),
        ),
    ]