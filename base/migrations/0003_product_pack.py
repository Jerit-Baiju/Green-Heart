# Generated by Django 4.0.6 on 2022-07-05 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_product_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pack',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.productpack'),
        ),
    ]
