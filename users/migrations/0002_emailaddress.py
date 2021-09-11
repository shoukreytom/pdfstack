# Generated by Django 3.1.5 on 2021-09-11 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('token', models.CharField(max_length=120, unique=True)),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
    ]
