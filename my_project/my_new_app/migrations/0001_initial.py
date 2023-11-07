# Generated by Django 4.2.6 on 2023-11-07 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30, verbose_name='Email')),
                ('password', models.CharField(max_length=40, verbose_name='Пароль')),
            ],
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=256, verbose_name='Задание')),
                ('taskAll', models.TextField(verbose_name='Описание')),
                ('date', models.DateField(verbose_name='Дата окончания')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_new_app.users')),
            ],
        ),
    ]
