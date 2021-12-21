# Generated by Django 2.2 on 2021-12-21 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('applications', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('state', models.BooleanField()),
                ('effective_date', models.DateField()),
                ('discounts', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Discounts')),
            ],
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_period', models.DateField(auto_now_add=True)),
                ('end_period', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('discounts_applied', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Discounts')),
                ('partner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Partner')),
            ],
        ),
        migrations.AddField(
            model_name='partner',
            name='plane',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Plane'),
        ),
    ]