# Generated by Django 3.2.6 on 2021-08-04 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_time_stamp', models.DateTimeField(blank=True, null=True, verbose_name='delete date')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='is deleted')),
                ('name', models.CharField(help_text='enter the brand name', max_length=50, unique=True, verbose_name='brand name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Categori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_time_stamp', models.DateTimeField(blank=True, null=True, verbose_name='delete date')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='is deleted')),
                ('name', models.CharField(help_text='enter the category', max_length=100, unique=True, verbose_name='category name')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.categori', verbose_name='enter parent if exist')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_time_stamp', models.DateTimeField(blank=True, null=True, verbose_name='delete date')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='is deleted')),
                ('name', models.CharField(help_text='enter the discount', max_length=50, verbose_name='discount name')),
                ('discount', models.IntegerField(choices=[('toman', 'toman'), ('percent', 'percent')], help_text='enter the discount', verbose_name='discount')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DiscountCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_time_stamp', models.DateTimeField(blank=True, null=True, verbose_name='delete date')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='is deleted')),
                ('name', models.CharField(help_text='enter name for discount', max_length=50, verbose_name='discount code')),
                ('code', models.IntegerField(help_text=' enter code for discount ', unique=True, verbose_name='discount code')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_time_stamp', models.DateTimeField(blank=True, null=True, verbose_name='delete date')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='is deleted')),
                ('price', models.PositiveIntegerField(help_text='enter the price', verbose_name='price')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_time_stamp', models.DateTimeField(blank=True, null=True, verbose_name='delete date')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='is deleted')),
                ('name', models.CharField(help_text='enter product name', max_length=200, verbose_name='name')),
                ('image', models.FileField(help_text='put picture for product', upload_to='Product/', verbose_name='image')),
                ('inventory', models.PositiveIntegerField(verbose_name='Inventory')),
                ('view', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='view')),
                ('inavailable', models.BooleanField(verbose_name='inavailable')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.brand', verbose_name='barnd name')),
                ('category', models.ForeignKey(help_text='enter the category', on_delete=django.db.models.deletion.CASCADE, to='product.categori', verbose_name='category')),
                ('discount', models.ForeignKey(help_text='enter the discount', on_delete=django.db.models.deletion.CASCADE, to='product.discount', verbose_name='discount')),
                ('price', models.ForeignKey(help_text='enter the price', on_delete=django.db.models.deletion.CASCADE, to='product.price', verbose_name='price')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
