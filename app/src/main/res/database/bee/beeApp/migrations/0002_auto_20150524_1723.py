# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='icon',
            field=models.ImageField(upload_to='/Users/vddm/Documents/forkBEE/BEE/app/src/main/res/database/bee/media/images/'),
        ),
    ]
