# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nonveg', models.CharField(max_length=30)),
                ('Veg', models.CharField(max_length=30)),
                ('pickles', models.CharField(max_length=35)),
            ],
        ),
    ]
