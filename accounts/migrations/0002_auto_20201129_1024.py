# Generated by Django 3.1.3 on 2020-11-29 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account_number',
            field=models.IntegerField(blank=True, default=562731002402),
        ),
    ]
