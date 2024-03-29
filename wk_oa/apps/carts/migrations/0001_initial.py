# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-29 06:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_goods_num', models.IntegerField(default=1, verbose_name='商品数量')),
                ('checked', models.BooleanField(default=True, verbose_name='是否被选中')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='用户')),
            ],
            options={
                'verbose_name': '购物车模型',
                'verbose_name_plural': '购物车模型',
                'db_table': 'wklc_carts',
            },
        ),
    ]
