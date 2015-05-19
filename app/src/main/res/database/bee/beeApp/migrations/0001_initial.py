# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(unique=True, verbose_name='nome', max_length=100)),
                ('description', models.CharField(verbose_name='descrição', max_length=300)),
                ('icon', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('text', models.TextField(verbose_name='comentário', max_length=400)),
                ('likes', models.PositiveIntegerField(verbose_name='curtidas')),
                ('date_hour', models.DateTimeField(verbose_name='data e hora da criação')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='nome', max_length=100)),
                ('nickname', models.CharField(unique=True, verbose_name='nome visível', max_length=100)),
                ('birth_date', models.DateField(verbose_name='data de nascimento')),
                ('gender', models.CharField(default='A', verbose_name='gênero', max_length=1, choices=[('F', 'Feminino'), ('M', 'Masculino'), ('A', 'Anônimo')])),
                ('sexuality', models.CharField(choices=[('HT', 'Héterossexual'), ('H', 'Homossexual'), ('B', 'Bissexual'), ('T', 'Transexual'), ('P', 'Pansexual')], verbose_name='opção sexual', max_length=2)),
                ('picture', models.ImageField(upload_to='')),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('anonymous', models.BooleanField(default=True)),
                ('badges', models.ManyToManyField(related_name='have_author', to='beeApp.Badge')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('text', models.TextField(verbose_name='texto', max_length=1000)),
                ('likes', models.PositiveIntegerField(verbose_name='curtidas')),
                ('date_hour', models.DateTimeField(verbose_name='data e hora de criação')),
                ('author', models.ForeignKey(related_name='have_author_post', to='beeApp.Person')),
                ('post_likes', models.ManyToManyField(related_name='likes_person_post', to='beeApp.Person')),
                ('post_reports', models.ManyToManyField(related_name='reports_person_post', to='beeApp.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(unique=True, verbose_name='titulo', max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='beeApp.Tag'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(related_name='have_author_comment', to='beeApp.Person'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_likes',
            field=models.ManyToManyField(related_name='likes_person_comment', to='beeApp.Person'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_reports',
            field=models.ManyToManyField(related_name='reports_person_comment', to='beeApp.Person'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(related_name='have_post', to='beeApp.Post'),
        ),
    ]
