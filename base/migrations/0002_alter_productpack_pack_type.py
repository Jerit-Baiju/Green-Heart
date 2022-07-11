# Generated by Django 4.0.6 on 2022-07-11 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpack',
            name='pack_type',
            field=models.CharField(choices=[('KG', 'KG'), ('LTR', 'LTR'), ('ML', 'ML')], default='LTR', max_length=10),
        ),
    ]