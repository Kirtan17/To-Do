# Generated by Django 3.1.4 on 2021-01-01 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
