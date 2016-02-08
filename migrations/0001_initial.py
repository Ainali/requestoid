# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-07 02:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_id', models.IntegerField()),
                ('cat_title', models.CharField(max_length=255)),
                ('wiki', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('user_id', models.IntegerField()),
                ('timestamp', models.CharField(max_length=14)),
                ('action', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('user_id', models.IntegerField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_id', models.IntegerField()),
                ('page_title', models.CharField(max_length=255)),
                ('user_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=255)),
                ('wiki', models.CharField(max_length=63)),
                ('timestamp', models.CharField(max_length=14)),
                ('summary', models.CharField(max_length=160)),
                ('status', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WikiProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.IntegerField()),
                ('project_title', models.CharField(max_length=255)),
                ('wiki', models.CharField(max_length=63)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requestoid.Requests')),
            ],
        ),
        migrations.AddField(
            model_name='notes',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requestoid.Requests'),
        ),
        migrations.AddField(
            model_name='logs',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requestoid.Requests'),
        ),
        migrations.AddField(
            model_name='categories',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requestoid.Requests'),
        ),
    ]