# Generated by Django 3.1 on 2021-03-16 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20210314_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title_ky',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
