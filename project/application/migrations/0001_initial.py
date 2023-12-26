# Generated by Django 5.0 on 2023-12-26 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.IntegerField(verbose_name='telegram id')),
                ('full_name', models.CharField(max_length=255, verbose_name='Полное имя пользователя')),
                ('user_name', models.CharField(max_length=255, verbose_name='Имя пользователя')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255, verbose_name='Cлово')),
                ('translated_word', models.CharField(max_length=255, verbose_name='Переведенное слово')),
                ('translated_language', models.CharField(max_length=255, verbose_name='C языка')),
                ('translated_to_language', models.CharField(max_length=255, verbose_name='Переведен на')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.profile', verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'Слово',
                'verbose_name_plural': 'Слова',
            },
        ),
    ]