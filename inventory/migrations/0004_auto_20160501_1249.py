# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='color',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='variation',
            name='size',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
    ]
