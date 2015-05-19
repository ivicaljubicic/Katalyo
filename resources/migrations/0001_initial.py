# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('StreetName', models.CharField(max_length=200)),
                ('Number', models.CharField(max_length=20)),
                ('Zip', models.IntegerField()),
                ('Country', models.CharField(max_length=3)),
                ('CreatedBy', models.CharField(max_length=200)),
                ('CreatedDateTime', models.DateTimeField(auto_now_add=True)),
                ('ChangedBy', models.CharField(max_length=200)),
                ('ChangedDateTime', models.DateTimeField(auto_now=True)),
                ('Status', models.CharField(max_length=20)),
                ('Version', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Organisations',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('Name', models.CharField(max_length=200)),
                ('Description', models.TextField()),
                ('Country', models.CharField(max_length=3)),
                ('Industry', models.CharField(max_length=3)),
                ('DefaultLang', models.CharField(max_length=10)),
                ('Purpose', models.CharField(max_length=200)),
                ('CreatedBy', models.CharField(max_length=200)),
                ('CreatedDateTime', models.DateTimeField(auto_now_add=True)),
                ('ChangedBy', models.CharField(max_length=200)),
                ('ChangedDateTime', models.DateTimeField(auto_now=True)),
                ('Status', models.CharField(max_length=20)),
                ('Version', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ResourceDef',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('CreatedBy', models.CharField(max_length=200)),
                ('CreatedDateTime', models.DateTimeField(auto_now_add=True)),
                ('ChangedBy', models.CharField(max_length=200)),
                ('ChangedDateTime', models.DateTimeField(auto_now=True)),
                ('Status', models.CharField(max_length=20)),
                ('Version', models.IntegerField()),
                ('Private', models.BooleanField()),
                ('ResourceType', models.CharField(max_length=1)),
                ('DefaultLang', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceDefFields',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('FieldType', models.CharField(max_length=200)),
                ('GenericType', models.CharField(max_length=200)),
                ('DBType', models.CharField(max_length=200)),
                ('Status', models.CharField(max_length=200)),
                ('SeqNo', models.IntegerField()),
                ('CreatedBy', models.CharField(max_length=200)),
                ('CreatedDateTime', models.DateTimeField(auto_now_add=True)),
                ('ChangedBy', models.CharField(max_length=200)),
                ('ChangedDateTime', models.DateTimeField(auto_now=True)),
                ('Version', models.IntegerField()),
                ('Resource', models.ForeignKey(to='resources.ResourceDef')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceDefFieldsLang',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('Lang', models.CharField(max_length=10)),
                ('Name', models.CharField(max_length=200)),
                ('Subject', models.CharField(max_length=1000)),
                ('Description', models.TextField()),
                ('CreatedBy', models.CharField(max_length=200)),
                ('CreatedDateTime', models.DateTimeField(auto_now_add=True)),
                ('ChangedBy', models.CharField(max_length=200)),
                ('ChangedDateTime', models.DateTimeField(auto_now=True)),
                ('Version', models.IntegerField()),
                ('ResourceDefFields', models.ForeignKey(to='resources.ResourceDefFields')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceDefLang',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('Lang', models.CharField(max_length=10)),
                ('Name', models.CharField(max_length=200)),
                ('Subject', models.CharField(max_length=1000)),
                ('Description', models.TextField()),
                ('CreatedBy', models.CharField(max_length=200)),
                ('CreatedDateTime', models.DateTimeField(auto_now_add=True)),
                ('ChangedBy', models.CharField(max_length=200)),
                ('ChangedDateTime', models.DateTimeField(auto_now=True)),
                ('Version', models.IntegerField()),
                ('Resource', models.ForeignKey(to='resources.ResourceDef')),
            ],
        ),
        migrations.AddField(
            model_name='addresses',
            name='Organisation',
            field=models.ForeignKey(to='resources.Organisations'),
        ),
    ]
