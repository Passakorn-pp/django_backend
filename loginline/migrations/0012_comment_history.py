# Generated by Django 3.1.7 on 2021-03-11 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginline', '0011_remove_userline_type_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dormitory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginline.dormitory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginline.userline')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('dormitory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginline.dormitory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginline.userline')),
            ],
        ),
    ]
