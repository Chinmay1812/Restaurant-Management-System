# Generated by Django 3.1.3 on 2020-11-23 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginhandle', '0003_mylist'),
    ]

    operations = [
        migrations.CreateModel(
            name='mysale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('profit', models.IntegerField()),
            ],
        ),
    ]
