# Generated by Django 2.1.7 on 2019-05-14 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20190513_0034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ('user',), 'verbose_name': 'profile', 'verbose_name_plural': '用户2'},
        ),
        migrations.AlterModelOptions(
            name='wechattag',
            options={'ordering': ('wechat_tag_id',), 'verbose_name': 'wechatTag', 'verbose_name_plural': '企业号标签'},
        ),
    ]
