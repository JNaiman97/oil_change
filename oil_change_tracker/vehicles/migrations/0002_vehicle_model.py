# Generated by Django 5.1.7 on 2025-04-07 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='model',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
