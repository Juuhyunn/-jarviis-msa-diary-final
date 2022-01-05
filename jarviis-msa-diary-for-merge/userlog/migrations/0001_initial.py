# Generated by Django 3.2.5 on 2021-11-30 07:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField()),
                ('address', models.TextField()),
                ('x', models.TextField()),
                ('y', models.TextField()),
                ('log_date', models.DateTimeField(default=datetime.datetime(2021, 11, 30, 16, 54, 7, 955714))),
                ('weather', models.TextField()),
                ('log_type', models.TextField()),
                ('contents', models.TextField()),
                ('user_id', models.IntegerField()),
            ],
            options={
                'db_table': 'userlog',
            },
        ),
    ]