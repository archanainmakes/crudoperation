# Generated by Django 3.2.19 on 2023-06-08 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slno', models.IntegerField()),
                ('itemname', models.CharField(max_length=250)),
                ('desc', models.TextField()),
            ],
        ),
    ]
