# Generated by Django 2.1.7 on 2019-07-03 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0002_auto_20190519_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='help',
            name='available',
            field=models.BooleanField(default=True, verbose_name='状态'),
        ),
    ]