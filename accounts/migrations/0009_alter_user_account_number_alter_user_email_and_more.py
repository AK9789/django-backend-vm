# Generated by Django 4.1.6 on 2023-02-08 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20201205_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account_number',
            field=models.IntegerField(blank=True, default=442506913621),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]