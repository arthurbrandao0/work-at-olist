# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent_category_id',
            field=models.IntegerField(null=True),
        ),
    ]
