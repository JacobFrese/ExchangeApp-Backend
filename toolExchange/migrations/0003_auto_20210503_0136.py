# Generated by Django 3.0.9 on 2021-05-03 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolExchange', '0002_tool_live'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='live',
            field=models.BooleanField(default=True),
        ),
    ]