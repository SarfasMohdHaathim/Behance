# Generated by Django 4.1.3 on 2022-12-08 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('dp', models.ImageField(blank=True, default='profiles/download_1.jpeg', null=True, upload_to='profiles/')),
                ('coverimage', models.ImageField(blank=True, default='covers/images.png', null=True, upload_to='covers/')),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('facebook', models.CharField(blank=True, max_length=200, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=200, null=True)),
                ('twitter', models.CharField(blank=True, max_length=200, null=True)),
                ('dribbble', models.CharField(blank=True, max_length=200, null=True)),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
