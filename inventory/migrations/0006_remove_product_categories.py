# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
    ]
