# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Javvadhicp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.CharField(default=b'', max_length=5),
        ),
    ]
