# Generated by Django 3.0.6 on 2020-06-24 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200624_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_time',
            field=models.DateField(blank=True, null=True),
        ),
    ]
