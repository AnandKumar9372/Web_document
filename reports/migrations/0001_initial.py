# Generated by Django 2.2 on 2022-12-15 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MobileList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=25)),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=25)),
                ('ram', models.CharField(max_length=25)),
            ],
        ),
    ]
