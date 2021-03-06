# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import eggplant.market.models.inventory


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to=eggplant.market.models.inventory.do_upload_product_image, null=True),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
