# Generated by Django 4.0.2 on 2022-03-30 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.IntegerField(default=-1),
        ),
    ]
