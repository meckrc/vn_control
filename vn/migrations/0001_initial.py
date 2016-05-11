# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mftp_log',
            fields=[
                ('f_id', models.AutoField(primary_key=True, serialize=False)),
                ('f_number', models.IntegerField(blank=True, null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440')),
                ('f_package', models.CharField(max_length=12, verbose_name='\u041a\u043e\u043d\u0432\u0435\u0440\u0442')),
                ('f_size', models.CharField(max_length=12, verbose_name='\u0420\u0430\u0437\u043c\u0435\u0440')),
                ('f_type', models.CharField(max_length=25, verbose_name='\u0422\u0438\u043f')),
                ('f_date', models.DateField(verbose_name='\u0414\u0430\u0442\u0430')),
                ('f_time', models.TimeField(verbose_name='\u0412\u0440\u0435\u043c\u044f')),
                ('f_source', models.CharField(max_length=50, verbose_name='\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044c')),
                ('f_destination', models.CharField(max_length=50, verbose_name='\u041f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044c')),
            ],
            options={
                'db_table': 'mftp_log',
            },
        ),
    ]
