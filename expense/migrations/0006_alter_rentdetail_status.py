# Generated by Django 4.1 on 2022-09-07 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0005_alter_rentdetail_rent_type_alter_rentdetail_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentdetail',
            name='status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Not Paid', 'Not Paid')], default='Not Paid', max_length=50),
        ),
    ]
