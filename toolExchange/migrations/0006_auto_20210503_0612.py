# Generated by Django 3.0.9 on 2021-05-03 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolExchange', '0005_auto_20210503_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='description',
            field=models.CharField(max_length=2000),
        ),
    ]
