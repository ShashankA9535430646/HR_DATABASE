# Generated by Django 4.1.7 on 2023-04-10 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_model1_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model1',
            name='age',
            field=models.PositiveIntegerField(blank=True, max_length=100, null=True),
        ),
    ]
