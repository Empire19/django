# Generated by Django 4.2.2 on 2023-08-01 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_alter_employee_aadhar_alter_employee_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='branch_name',
            field=models.CharField(max_length=100),
        ),
    ]
