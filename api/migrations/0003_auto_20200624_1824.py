# Generated by Django 3.0.6 on 2020-06-24 16:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200624_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_time',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
