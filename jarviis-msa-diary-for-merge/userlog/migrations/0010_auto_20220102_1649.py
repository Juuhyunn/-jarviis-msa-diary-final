# Generated by Django 3.2.9 on 2022-01-02 07:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlog', '0009_alter_userlog_log_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlog',
            name='task_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userlog',
            name='log_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 2, 16, 49, 17, 998671)),
        ),
    ]
