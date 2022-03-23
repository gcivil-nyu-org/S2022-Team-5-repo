# Generated by Django 3.0.3 on 2022-03-19 02:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0002_listing_calendly_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
