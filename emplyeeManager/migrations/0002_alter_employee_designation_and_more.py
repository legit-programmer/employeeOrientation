# Generated by Django 4.1.1 on 2022-09-10 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplyeeManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='qualification',
            field=models.CharField(max_length=50),
        ),
    ]