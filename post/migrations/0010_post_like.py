# Generated by Django 4.1.3 on 2023-01-10 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]