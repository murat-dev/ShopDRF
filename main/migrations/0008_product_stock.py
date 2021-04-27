# Generated by Django 3.1 on 2021-03-13 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210313_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.CharField(choices=[('in stock', 'in stock'), ('out of stock', 'out of stock')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]