# Generated by Django 4.2.2 on 2023-07-04 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1997-11-05'),
            preserve_default=False,
        ),
    ]
