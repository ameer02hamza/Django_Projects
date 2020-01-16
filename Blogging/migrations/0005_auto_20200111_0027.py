# Generated by Django 2.2.5 on 2020-01-11 00:27

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Blogging', '0004_auto_20200111_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='post_Date',
            field=models.DateField(default=datetime.datetime(2020, 1, 11, 0, 27, 36, 114174, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_date',
            field=models.DateField(default=datetime.datetime(2020, 1, 11, 0, 27, 36, 143628, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='Blogging.blogs'),
        ),
    ]
