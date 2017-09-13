# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 09:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shadowsocks', '0002_aliveip_local'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=128, verbose_name='购买者')),
                ('purchtime', models.DateTimeField(auto_now_add=True, verbose_name='购买时间')),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shadowsocks.Shop')),
            ],
            options={
                'verbose_name_plural': '购买记录',
            },
        ),
    ]