# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-08 04:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pachong', '0005_zhihudaiguang_xiaobing'),
    ]

    operations = [
        migrations.AddField(
            model_name='zhihudaiguang',
            name='topic_id',
            field=models.IntegerField(default=0),
        ),
    ]