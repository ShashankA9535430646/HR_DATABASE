# Generated by Django 4.1.7 on 2023-04-10 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_model1_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model1',
            name='age',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
