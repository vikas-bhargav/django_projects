# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171028_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='projects',
            name='start_date',
            field=models.DateField(),
        ),
    ]
