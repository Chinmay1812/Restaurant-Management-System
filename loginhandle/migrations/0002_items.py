# Generated by Django 3.1.3 on 2020-11-17 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginhandle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('rawmaterialcost', models.IntegerField()),
            ],
        ),
    ]