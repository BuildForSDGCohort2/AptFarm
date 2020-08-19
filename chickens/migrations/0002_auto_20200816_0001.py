# Generated by Django 3.0.8 on 2020-08-15 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('procedures', '0001_initial'),
        ('chickens', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chicken',
            name='drugs',
            field=models.ManyToManyField(null=True, to='procedures.Drugs'),
        ),
        migrations.AddField(
            model_name='chicken',
            name='feed',
            field=models.ManyToManyField(null=True, to='procedures.Feed'),
        ),
        migrations.AddField(
            model_name='chicken',
            name='procedures',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='procedures.Procedures'),
        ),
        migrations.AddField(
            model_name='chicken',
            name='specie',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='chicken',
            name='vaccine',
            field=models.ManyToManyField(null=True, to='procedures.Vaccine'),
        ),
    ]
