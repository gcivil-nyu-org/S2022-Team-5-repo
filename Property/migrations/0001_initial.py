# Generated by Django 4.0.1 on 2022-04-20 01:38

import Property.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('address1', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Address_1')),
                ('address2', models.CharField(blank=True, max_length=120, null=True, verbose_name='Address_2')),
                ('borough', models.CharField(blank=True, max_length=120, null=True, verbose_name='Borough')),
                ('zipcode', models.CharField(blank=True, max_length=8, null=True, verbose_name='Zip Code')),
                ('latitude', models.CharField(blank=True, max_length=50, null=True, verbose_name='Latitude')),
                ('longitude', models.CharField(blank=True, max_length=50, null=True, verbose_name='Longitude')),
                ('rent', models.IntegerField(default=1, verbose_name='Rent')),
                ('area', models.FloatField(default=0, verbose_name='Area')),
                ('bedrooms', models.IntegerField(default=1, verbose_name='Bedrooms')),
                ('bathrooms', models.IntegerField(default=1, verbose_name='Bathrooms')),
                ('furnished', models.BooleanField(default=False, verbose_name='Furnished')),
                ('elevator', models.BooleanField(default=False, verbose_name='Elevator')),
                ('heating', models.BooleanField(default=False, verbose_name='Heating')),
                ('parking', models.BooleanField(default=False, verbose_name='Parking')),
                ('laundry', models.BooleanField(default=False, verbose_name='Laundry')),
                ('matterport_link', models.URLField(blank=True, max_length=300, null=True, verbose_name='Matterport_Link')),
                ('photo_url', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Upload Primary Image')),
                ('photo_url2', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Upload Second Image')),
                ('photo_url3', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Upload Third Image')),
                ('calendly_link', models.URLField(blank=True, max_length=300, null=True, verbose_name='Calendly_Link')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('active', models.BooleanField(default=False)),
                ('ratings', models.FloatField(blank=True, default=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RequestTour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default='N/A', max_length=32, verbose_name='First Name')),
                ('lastName', models.CharField(default='N/A', max_length=32, verbose_name='Last Name')),
                ('email', models.EmailField(default='N/A', max_length=254, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=12, null=True, verbose_name='Phone')),
                ('message', models.CharField(blank=True, max_length=500, null=True, verbose_name='Message')),
                ('tourDate', models.DateField(default=datetime.datetime.now, verbose_name='Tour Date')),
                ('listing', models.ForeignKey(default=Property.models.Listing, on_delete=django.db.models.deletion.CASCADE, to='Property.listing')),
            ],
        ),
    ]
