# Generated by Django 3.1.7 on 2021-03-23 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginline', '0028_auto_20210323_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datauser',
            name='year',
        ),
    ]