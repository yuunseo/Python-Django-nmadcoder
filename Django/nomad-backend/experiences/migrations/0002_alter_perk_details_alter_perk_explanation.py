# Generated by Django 4.2.3 on 2023-07-13 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perk',
            name='details',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='perk',
            name='explanation',
            field=models.TextField(blank=True, default=''),
        ),
    ]
