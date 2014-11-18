# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(max_length=5, verbose_name=b'\xe4\xba\xba\xe5\x91\x98\xe7\xb1\xbb\xe5\x9e\x8b'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=10, verbose_name=b'\xe5\xa4\x84\xe5\xae\xa4\xe5\x90\x8d\xe7\xa7\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='duty',
            name='name',
            field=models.CharField(max_length=5, verbose_name=b'\xe8\x81\x8c\xe5\x8a\xa1\xe5\x90\x8d\xe7\xa7\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='level',
            name='name',
            field=models.CharField(max_length=5, verbose_name=b'\xe7\xba\xa7\xe5\x88\xab\xe5\x90\x8d\xe7\xa7\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='begin_work_date',
            field=models.DateField(verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe5\xb7\xa5\xe4\xbd\x9c\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(verbose_name=b'\xe7\x94\x9f\xe6\x97\xa5'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='character',
            field=models.ForeignKey(verbose_name=b'\xe4\xba\xba\xe5\x91\x98\xe6\x80\xa7\xe8\xb4\xa8', to='account.Character'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='department',
            field=models.ForeignKey(verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8', to='account.Department'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='duty',
            field=models.ForeignKey(verbose_name=b'\xe8\x81\x8c\xe5\x8a\xa1', to='account.Duty'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='enter_date',
            field=models.DateField(verbose_name=b'\xe8\xbf\x9b\xe5\x85\xa5\xe6\x9c\xac\xe5\x8d\x95\xe4\xbd\x8d\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(max_length=1, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'M', b'\xe7\x94\xb7'), (b'F', b'\xe5\xa5\xb3')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='level',
            field=models.ForeignKey(verbose_name=b'\xe7\xba\xa7\xe5\x88\xab', to='account.Level'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(verbose_name=b'\xe8\xb4\xa6\xe5\x8f\xb7\xe4\xbf\xa1\xe6\x81\xaf', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
