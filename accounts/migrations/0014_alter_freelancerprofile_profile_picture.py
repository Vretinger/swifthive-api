# Generated by Django 5.1.4 on 2025-04-27 11:33

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_customuser_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancerprofile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(default='../default_profile_rnezic', max_length=255, verbose_name='images/'),
        ),
    ]
