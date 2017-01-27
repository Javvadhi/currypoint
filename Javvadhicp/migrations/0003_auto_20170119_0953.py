# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Javvadhicp', '0002_menu_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='NonVeg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=5)),
                ('quantity', models.CharField(max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]
