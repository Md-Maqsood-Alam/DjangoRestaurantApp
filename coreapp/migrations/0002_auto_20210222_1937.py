# Generated by Django 2.2 on 2021-02-22 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='dish',
            name='whetherNonVeg',
            field=models.BooleanField(default=True),
        ),
    ]
