# Generated by Django 2.1.7 on 2019-05-14 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20190514_0926'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='权限')),
                ('slug', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'verbose_name_plural': '权限',
            },
        ),
        migrations.CreateModel(
            name='NoPayDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='权限')),
                ('slug', models.CharField(blank=True, max_length=25, null=True)),
                ('days', models.PositiveIntegerField(blank=True, max_length=3, null=True, verbose_name='天数')),
            ],
            options={
                'verbose_name_plural': '未支付时间设置',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='group2',
            field=models.ManyToManyField(blank=True, null=True, related_name='group2', to='login.Group2', verbose_name='权限'),
        ),
    ]
