# Generated by Django 2.2 on 2021-02-25 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='zip',
            field=models.CharField(max_length=6),
        ),
    ]
