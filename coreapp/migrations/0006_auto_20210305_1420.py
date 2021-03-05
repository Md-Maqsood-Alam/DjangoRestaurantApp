# Generated by Django 2.2 on 2021-03-05 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20210226_0037'),
        ('coreapp', '0005_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='customers.Customer'),
            preserve_default=False,
        ),
    ]