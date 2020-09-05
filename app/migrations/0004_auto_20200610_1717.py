# Generated by Django 3.0.7 on 2020-06-10 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_blogg'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogg',
            name='writer',
            field=models.CharField(default='VNM', max_length=400),
        ),
        migrations.AlterField(
            model_name='blogg',
            name='summary',
            field=models.CharField(max_length=400),
        ),
    ]