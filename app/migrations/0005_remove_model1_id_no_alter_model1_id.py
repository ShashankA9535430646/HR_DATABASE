# Generated by Django 4.1.7 on 2023-04-07 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_model1_id_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model1',
            name='id_no',
        ),
        migrations.AlterField(
            model_name='model1',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]