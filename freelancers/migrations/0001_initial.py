# Generated by Django 5.1.4 on 2024-12-30 14:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('experience', models.TextField(blank=True, null=True)),
                ('portfolio_link', models.URLField(blank=True, null=True)),
                ('hourly_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('availability_status', models.CharField(choices=[('Available', 'Available'), ('Busy', 'Busy'), ('On Leave', 'On Leave')], default='Available', max_length=20)),
                ('profile_picture', models.ImageField(default='../default_profile_rnezic', upload_to='freelancer_pics/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('skills', models.ManyToManyField(blank=True, to='freelancers.skill')),
            ],
        ),
    ]
