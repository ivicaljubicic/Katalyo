# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcedef',
            name='Organisation',
            field=models.ForeignKey(to='resources.Organisations', default=1),
            preserve_default=False,
        ),
    ]
