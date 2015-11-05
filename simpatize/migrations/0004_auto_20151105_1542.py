# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpatize', '0003_placekind'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PlaceKind',
        ),
        migrations.RemoveField(
            model_name='place',
            name='likes',
        ),
        migrations.AddField(
            model_name='place',
            name='types',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='vicinity',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
