# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-14 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0013_auto_20160314_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='userac',
            name='user_m_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
