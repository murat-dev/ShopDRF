# Generated by Django 3.1 on 2021-03-11 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0002_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
