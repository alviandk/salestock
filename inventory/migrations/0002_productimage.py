# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import inventory.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=inventory.models.image_upload_to)),
                ('product', models.ForeignKey(to='inventory.Product')),
            ],
        ),
    ]
