# Generated by Django 2.2 on 2021-12-22 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20211222_0243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pay',
            name='amount',
        ),
    ]
