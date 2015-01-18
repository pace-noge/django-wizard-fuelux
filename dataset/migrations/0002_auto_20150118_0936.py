# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articleproperty',
            old_name='property',
            new_name='value',
        ),
    ]
