# Generated by Django 3.1.3 on 2023-09-04 02:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 4, 2, 8, 33, 170473, tzinfo=utc)),
        ),
    ]
