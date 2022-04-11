# Generated by Django 4.0.1 on 2022-04-10 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='photo_url',
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads', verbose_name='Image')),
                ('listing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Property.listing')),
            ],
        ),
    ]
