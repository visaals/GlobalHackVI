# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 08:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rssfeed', '0002_item_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='text',
            new_name='description',
        ),
    ]