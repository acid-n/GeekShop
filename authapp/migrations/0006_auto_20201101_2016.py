# Generated by Django 3.1.1 on 2020-11-01 20:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20201028_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 3, 20, 16, 36, 590642, tzinfo=utc)),
        ),
    ]
