# Generated by Django 4.0.1 on 2022-03-30 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0002_alter_user_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.IntegerField(default=-1, null=True),
        ),
    ]
