# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 04:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0022_user_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_log',
            name='produ',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.product'),
        ),
    ]