# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 10:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0019_imagee_ps_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagee',
            name='ps_id',
        ),
    ]