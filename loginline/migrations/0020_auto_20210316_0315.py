# Generated by Django 3.1.7 on 2021-03-15 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginline', '0019_room_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='img',
            field=models.CharField(default='https://sv1.picz.in.th/images/2021/03/14/D12sTl.png', max_length=1000),
        ),
    ]
