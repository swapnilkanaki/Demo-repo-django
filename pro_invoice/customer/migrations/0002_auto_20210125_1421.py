# Generated by Django 3.1.3 on 2021-01-25 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='website',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
