# Generated by Django 3.1.3 on 2023-09-18 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0003_auto_20230904_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='create_date',
            field=models.DateTimeField(),
        ),
    ]
