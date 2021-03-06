# Generated by Django 3.2.5 on 2021-07-29 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer_a', models.CharField(max_length=150)),
                ('answer_b', models.CharField(max_length=150)),
                ('answer_c', models.CharField(max_length=150)),
                ('answer_d', models.CharField(max_length=150)),
                ('good_answer', models.CharField(max_length=150)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.category')),
            ],
        ),
        migrations.CreateModel(
            name='LeaderBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('points', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.category')),
            ],
        ),
    ]
