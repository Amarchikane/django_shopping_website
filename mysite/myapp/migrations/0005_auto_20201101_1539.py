# Generated by Django 3.1.2 on 2020-11-01 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20201030_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Address',
            field=models.CharField(default='adress', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=35),
        ),
    ]
