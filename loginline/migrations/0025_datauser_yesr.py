# Generated by Django 3.1.7 on 2021-03-23 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginline', '0024_auto_20210323_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='datauser',
            name='yesr',
            field=models.IntegerField(default=''),
            preserve_default=False,
        ),
    ]