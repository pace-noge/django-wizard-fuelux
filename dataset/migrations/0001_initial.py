# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('headline',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticleProperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('property', models.CharField(max_length=100)),
                ('article', models.ForeignKey(to='dataset.Article')),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('title',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='publications',
            field=models.ManyToManyField(to='dataset.Publication'),
            preserve_default=True,
        ),
    ]
