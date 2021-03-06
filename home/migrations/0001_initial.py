# Generated by Django 3.1.3 on 2020-12-06 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reason_approved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
                ('display_name', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='reason_unapproved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
                ('display_name', models.TextField(max_length=10)),
            ],
        ),
    ]
