# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_remove_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variation',
            name='sale_price',
        ),
    ]
