# Generated by Django 4.1.1 on 2022-09-14 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplyeeManager', '0006_alter_employee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
