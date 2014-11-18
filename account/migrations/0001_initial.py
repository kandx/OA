# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=5)),
                ('create_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'cbd_character',
                'verbose_name': '\u4eba\u5458\u6027\u8d28',
                'verbose_name_plural': '\u4eba\u5458\u6027\u8d28',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'cbd_department',
                'verbose_name': '\u5904\u5ba4',
                'verbose_name_plural': '\u5904\u5ba4',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Duty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=5)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'cbd_duty',
                'verbose_name': '\u804c\u52a1',
                'verbose_name_plural': '\u804c\u52a1',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=5)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'cbd_level',
                'verbose_name': '\u7ea7\u522b',
                'verbose_name_plural': '\u7ea7\u522b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'\xe7\x94\xb7'), (b'F', b'\xe5\xa5\xb3')])),
                ('birthday', models.DateField()),
                ('enter_date', models.DateField()),
                ('begin_work_date', models.DateField()),
                ('character', models.ForeignKey(to='account.Character')),
                ('department', models.ForeignKey(to='account.Department')),
                ('duty', models.ForeignKey(to='account.Duty')),
                ('level', models.ForeignKey(to='account.Level')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cbd_profile',
                'verbose_name': '\u4e2a\u4eba\u4fe1\u606f',
                'verbose_name_plural': '\u4e2a\u4eba\u4fe1\u606f',
            },
            bases=(models.Model,),
        ),
    ]
