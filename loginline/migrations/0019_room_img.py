# Generated by Django 3.1.7 on 2021-03-15 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginline', '0018_auto_20210316_0253'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='img',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
