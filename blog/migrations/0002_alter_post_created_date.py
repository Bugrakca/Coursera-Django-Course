# Generated by Django 3.2.4 on 2021-09-30 18:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 30, 18, 7, 23, 239765, tzinfo=utc)),
        ),
    ]
