# Generated by Django 3.0.3 on 2022-03-19 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0003_listing_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='bathroom',
            new_name='bathrooms',
        ),
    ]