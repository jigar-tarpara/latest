# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 06:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0014_userac_user_m_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_user',
            fields=[
                ('o_user_id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.IntegerField()),
                ('o_order_id', models.ManyToManyField(to='adminpanel.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.userac')),
            ],
        ),
    ]
