# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpatize', '0002_place_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceKind',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('kind', models.CharField(max_length=200)),
            ],
        ),
    ]
