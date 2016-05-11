# coding: utf-8


from __future__ import unicode_literals
from django.db import models
# from django.contrib.auth.models import User


class mftp_log(models.Model):
    f_id = models.AutoField(primary_key=True)
    f_number = models.IntegerField(verbose_name='Номер', blank=True, null=True)
    f_package = models.CharField(verbose_name='Конверт', max_length=12)
    f_size = models.CharField(verbose_name='Размер', max_length=12)
    f_type = models.CharField(verbose_name='Тип', max_length=25)
    f_date = models.DateField(verbose_name='Дата',)
    f_time = models.TimeField(verbose_name='Время',)
    f_source = models.CharField(verbose_name='Отправитель', max_length=50)
    f_destination = models.CharField(verbose_name='Получатель', max_length=50)

    class Meta:
        db_table = 'mftp_log'

'''
class TOrg(models.Model):
    f_id = models.AutoField(primary_key=True)
    f_org_type =  models.OneToOneField(LTypeOrg1, verbose_name="Тип учреждения",)
    f_reg =  models.OneToOneField(LReg1, verbose_name="Район",)
    f_short_name = models.CharField(verbose_name="Краткое наименование", max_length=50)
    f_long_name = models.CharField(verbose_name="Полное наименование", max_length=255)
    f_postcode = models.CharField(verbose_name="Почтовый индекс", max_length=6)
    f_city = models.CharField(verbose_name="Населенный пункт", max_length=30)
    f_address = models.CharField(verbose_name="Адрес", max_length=255)
    f_dir = models.IntegerField(verbose_name="Директор", blank=True, null=True)
    f_phone = models.CharField(verbose_name="Телефон", max_length=15)
    f_fax = models.CharField(verbose_name="Факс", max_length=15)

    class Meta:
        db_table = 't_org'
'''