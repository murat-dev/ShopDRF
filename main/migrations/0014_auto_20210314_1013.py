# Generated by Django 3.1 on 2021-03-14 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0007_auto_20210313_1806'),
        ('main', '0013_auto_20210314_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='myprofile.profilecustomer'),
        ),
    ]