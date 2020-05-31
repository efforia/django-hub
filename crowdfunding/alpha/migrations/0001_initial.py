# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 20:28
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'@@', max_length=100)),
                ('value', models.IntegerField(default=1)),
                ('description', models.TextField(default=b'', max_length=500)),
                ('deadline', models.DateTimeField(default=datetime.date(2017, 2, 28))),
                ('location', models.CharField(default=b'', max_length=200)),
                ('event_id', models.CharField(default=b'', max_length=50)),
                ('occurred', models.BooleanField(default=False)),
                ('visual', models.CharField(default=b'', max_length=150)),
                ('increased', models.BooleanField(default=False)),
                ('postponed', models.BooleanField(default=False)),
                ('min', models.IntegerField(default=2)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default=b'', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'', max_length=50)),
                ('start_time', models.DateTimeField(default=datetime.date(2017, 2, 28))),
                ('end_time', models.DateTimeField(default=datetime.date(2017, 2, 28))),
                ('event_id', models.CharField(default=b'me', max_length=50)),
                ('content', models.TextField(default=b'')),
                ('credit', models.IntegerField(default=0)),
                ('ytoken', models.CharField(default=b'', max_length=15)),
                ('visual', models.CharField(default=b'', max_length=100)),
                ('funded', models.BooleanField(default=False)),
                ('postponed', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Promoted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'@#', max_length=2)),
                ('prom', models.IntegerField(default=1)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='movement',
            name='cause',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='alpha.Project'),
        ),
        migrations.AddField(
            model_name='movement',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='interest',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alpha.Project'),
        ),
    ]