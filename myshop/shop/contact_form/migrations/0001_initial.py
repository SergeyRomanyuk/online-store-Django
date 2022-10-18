# Generated by Django 4.1.1 on 2022-10-13 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFRM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='Ваше имя')),
                ('tele', models.IntegerField(max_length=200, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('message', models.TextField(max_length=1000, verbose_name='Сообщение')),
            ],
        ),
    ]
