# Generated by Django 4.2.7 on 2023-12-05 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                # ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('completed', models.BooleanField()),
            ],
        ),
    ]