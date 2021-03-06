# Generated by Django 3.2.6 on 2021-08-05 22:58

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
            name='StoryCounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.IntegerField()),
            ],
            options={
                'ordering': ('-start',),
            },
        ),
        migrations.CreateModel(
            name='StoryID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_id', models.CharField(max_length=50, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-list_id',),
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('descendants', models.IntegerField()),
                ('kids', models.JSONField()),
                ('score', models.IntegerField()),
                ('link', models.TextField()),
                ('time_created', models.DateTimeField()),
                ('title', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('story_id', models.IntegerField(unique=True)),
                ('writer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name', 'time_created', 'type', 'title'),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('kids', models.JSONField()),
                ('comment_id', models.IntegerField(unique=True)),
                ('comment', models.TextField()),
                ('comment_time', models.DateTimeField()),
                ('type', models.CharField(max_length=50)),
                ('story_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='news.story', to_field='story_id')),
            ],
            options={
                'ordering': ('name', 'comment_time'),
            },
        ),
    ]
