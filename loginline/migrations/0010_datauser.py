# Generated by Django 3.1.7 on 2021-03-11 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginline', '0009_filterdo_tv'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=50)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginline.userline')),
            ],
        ),
    ]
