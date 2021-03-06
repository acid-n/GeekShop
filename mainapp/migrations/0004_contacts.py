# Generated by Django 3.1.1 on 2020-10-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20200929_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='название')),
                ('city', models.CharField(max_length=64, verbose_name='город')),
                ('email', models.CharField(max_length=64, unique=True, verbose_name='email')),
                ('phone', models.CharField(max_length=64, unique=True, verbose_name='телефон')),
                ('address', models.CharField(blank=True, max_length=128, verbose_name='адрес')),
            ],
            options={
                'verbose_name': 'контакты',
                'verbose_name_plural': 'контакты',
            },
        ),
    ]
