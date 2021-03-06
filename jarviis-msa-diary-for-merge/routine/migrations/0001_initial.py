# Generated by Django 3.2.5 on 2021-11-30 07:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userlog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=datetime.datetime(2021, 11, 30, 16, 54, 7, 954714))),
                ('log_repeat', models.IntegerField()),
                ('event_repeat', models.IntegerField()),
                ('priority', models.IntegerField()),
                ('grade', models.IntegerField()),
                ('contents', models.TextField()),
                ('cron', models.TextField()),
                ('event_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('log_id', models.ForeignKey(db_column='log_id', on_delete=django.db.models.deletion.CASCADE, to='userlog.userlog')),
            ],
            options={
                'db_table': 'routine',
            },
        ),
    ]
