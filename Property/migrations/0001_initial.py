# Generated by Django 4.0.1 on 2022-04-04 17:44

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields==[
                ('listing_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=-1, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('address1', models.CharField(default=-1, max_length=100)),
                ('address2', models.CharField(default=-1, max_length=120)),
                ('borough', models.CharField(default=-1, max_length=120)),
                ('zipcode', models.CharField(default=-1, max_length=8)),
                ('latitude', models.CharField(default='', max_length=300)),
                ('longitude', models.CharField(default='', max_length=300)),
                ('rent', models.IntegerField(default=-1)),
                ('description', models.CharField(default='-', max_length=300)),
                ('bedrooms', models.IntegerField(default=-1)),
                ('furnished', models.BooleanField(default=False)),
                ('elevator', models.BooleanField(default=False)),
                ('heating', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=False)),
                ('laundry', models.BooleanField(default=False)),
                ('ratings', models.FloatField(default=-1)),
                ('bathrooms', models.IntegerField(default=-1)),
                ('area', models.FloatField(default=-1)),
                ('active', models.BooleanField(default=False)),
                ('map_url', models.CharField(default='-', max_length=300)),
                ('photo_url', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('matterport_link', models.CharField(default=-1, max_length=300)),
                ('calendly_link', models.CharField(default=-1, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='UserOfApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('uaddr', models.CharField(default='', max_length=100)),
                ('zip', models.CharField(default=0, max_length=6)),
                ('phone', models.CharField(default='0000000000', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('renter', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
