# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='entry',
            field=models.TextField(max_length=10000),
            preserve_default=True,
        ),
    ]
