# Generated by Django 2.2 on 2021-03-02 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0003_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='occasion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]