<<<<<<< HEAD
# Generated by Django 4.0.6 on 2022-07-06 17:12
=======
# Generated by Django 4.0.6 on 2022-07-07 16:21
>>>>>>> 22fb1924

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('name', models.CharField(blank=True, max_length=50, null=True, unique=True)),
=======
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images')),
>>>>>>> 22fb1924
            ],
        ),
        migrations.CreateModel(
            name='ProductCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Products')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.productcategory')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.company')),
                ('pack', models.ManyToManyField(to='base.productpack')),
=======
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, unique=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.product')),
>>>>>>> 22fb1924
            ],
        ),
    ]
