# Generated by Django 4.1 on 2022-09-05 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0004_alter_rent_final_rent_alter_rent_rent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentdetail',
            name='rent_type',
            field=models.CharField(choices=[('one sided', 'one sided'), ('two sided', 'two sided'), ('fix rent', 'fix rent')], max_length=50),
        ),
        migrations.AlterField(
            model_name='rentdetail',
            name='status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Not Paid', 'Not Paid')], max_length=50),
        ),
    ]
