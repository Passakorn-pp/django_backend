# Generated by Django 3.1.7 on 2021-03-30 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginline', '0028_auto_20210326_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='dormitory',
            name='preper',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]