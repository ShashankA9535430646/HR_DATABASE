# Generated by Django 4.1.7 on 2023-04-07 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_model1_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='model1',
            name='id_no',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
