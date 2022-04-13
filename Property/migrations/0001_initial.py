# Generated by Django 4.0.1 on 2022-04-13 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('listing_id', models.AutoField(primary_key=True, serialize=False)),
                ('address1', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address_1')),
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
                ('calendly_link', models.URLField(blank=True, max_length=300, null=True, verbose_name='Calendly_Link')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='Description')),
                ('active', models.BooleanField(default=False)),
                ('ratings', models.FloatField(blank=True, default=1, null=True)),
            ],
        ),
    ]
