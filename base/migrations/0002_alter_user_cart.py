# Generated by Django 4.0.6 on 2022-07-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cart',
            field=models.ManyToManyField(to='base.cartproduct'),
        ),
    ]
