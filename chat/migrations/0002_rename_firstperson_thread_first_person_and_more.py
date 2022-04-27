# Generated by Django 4.0.2 on 2022-04-26 22:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="thread",
            old_name="firstPerson",
            new_name="first_person",
        ),
        migrations.RenameField(
            model_name="thread",
            old_name="secondPerson",
            new_name="second_person",
        ),
        migrations.AlterUniqueTogether(
            name="thread",
            unique_together={("first_person", "second_person")},
        ),
    ]
