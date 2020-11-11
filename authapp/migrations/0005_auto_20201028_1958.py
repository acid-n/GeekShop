# Generated by Django 3.1.1 on 2020-10-28 19:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20201027_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 30, 19, 58, 56, 254890, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shopuserprofile',
            name='about_me',
            field=models.TextField(blank=True, verbose_name='обо мне'),
        ),
        migrations.AlterField(
            model_name='shopuserprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'М'), ('W', 'Ж')], max_length=1, verbose_name='пол'),
        ),
        migrations.AlterField(
            model_name='shopuserprofile',
            name='tagline',
            field=models.CharField(blank=True, max_length=128, verbose_name='тэги'),
        ),
    ]