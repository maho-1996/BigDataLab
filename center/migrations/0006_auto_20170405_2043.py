# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0005_auto_20170329_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='passage',
            name='passagePhone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='blogpassage',
            name='label',
            field=models.CharField(choices=[('newTech', '新科技'), ('Food', '食品安全'), ('health', '健康养生')], max_length=20),
        ),
        migrations.AlterField(
            model_name='passage',
            name='passageLabel',
            field=models.CharField(choices=[('newTech', '新科技'), ('Food', '食品安全'), ('health', '健康养生')], max_length=20),
        ),
        migrations.AlterField(
            model_name='passage',
            name='passageSource',
            field=models.CharField(choices=[('email', '邮件'), ('friendCicle', '朋友圈'), ('message', '短信')], max_length=20),
        ),
    ]
