# Generated by Django 3.1.7 on 2021-03-23 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginline', '0024_auto_20210323_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='datauser',
            name='year',
            field=models.IntegerField(default=1),
        ),
    ]
