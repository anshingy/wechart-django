# Generated by Django 2.1.7 on 2019-05-14 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20190514_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nopaydate',
            name='name',
            field=models.CharField(max_length=25, verbose_name='名称'),
        ),
    ]