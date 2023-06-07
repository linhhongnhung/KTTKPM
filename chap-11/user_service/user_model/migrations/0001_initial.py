# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-09-28 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
