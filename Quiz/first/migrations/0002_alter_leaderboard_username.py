# Generated by Django 3.2.5 on 2021-08-03 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaderboard',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
