# Generated by Django 2.1.7 on 2019-05-12 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0003_auto_20190512_1609'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productpricegroup',
            options={'ordering': ('name',), 'verbose_name': '价格组', 'verbose_name_plural': '价格组'},
        ),
        migrations.AddField(
            model_name='productpricegroup',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
