# Generated by Django 2.2.5 on 2020-01-07 14:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=50)),
                ('post_Date', models.DateField(default=datetime.datetime(2020, 1, 7, 14, 28, 56, 771203))),
                ('post_content', models.CharField(max_length=1200)),
                ('owner_email', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.CharField(max_length=500)),
                ('owner_username', models.CharField(max_length=15)),
                ('comment_date', models.DateField(default=datetime.datetime(2020, 1, 7, 14, 28, 57, 56680))),
            ],
        ),
    ]