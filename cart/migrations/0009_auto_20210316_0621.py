# Generated by Django 3.1 on 2021-03-16 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0007_auto_20210313_1806'),
        ('cart', '0008_auto_20210316_0615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='user',
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='myprofile.profilecustomer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cartitem', to='cart.cart'),
            preserve_default=False,
        ),
    ]
