# Generated by Django 3.1.7 on 2021-03-23 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginline', '0025_datauser_yesr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datauser',
            name='yesr',
        ),
    ]