# Generated by Django 4.1 on 2022-09-06 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0006_alter_passenger_joining_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='rent_type',
            field=models.CharField(choices=[('One sided', 'One sided'), ('Two sided', 'Two sided'), ('Fix rent', 'Fix rent')], max_length=10),
        ),
    ]
