# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-11 10:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0025_add'),
    ]

    operations = [
        migrations.CreateModel(
            name='pro_display',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.product')),
                ('subcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.alphasubcat')),
            ],
        ),
    ]
