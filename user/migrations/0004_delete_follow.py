# Generated by Django 4.1.3 on 2023-01-07 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_follow'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Follow',
        ),
    ]
