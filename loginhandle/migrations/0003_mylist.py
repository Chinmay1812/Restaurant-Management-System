# Generated by Django 3.1.3 on 2020-11-18 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginhandle', '0002_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='mylist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('rate', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('profit', models.IntegerField()),
            ],
        ),
    ]