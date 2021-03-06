# Generated by Django 3.2.6 on 2021-08-14 21:03

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_time_stamp', models.DateTimeField(blank=True, null=True, verbose_name='delete date')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('deleted', models.BooleanField(default=False, verbose_name='is deleted')),
                ('name', models.CharField(help_text='enter the brand name', max_length=50, unique=True, verbose_name='brand name')),
                ('image', models.FileField(help_text='put picture for brand', upload_to=product.models.brand_image_path, verbose_name='barnd image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_time_stamp', models.DateTimeField(blank=True, null=True, verbose_name='delete date')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('deleted', models.BooleanField(default=False, verbose_name='is deleted')),
                ('name', models.CharField(help_text='enter the category', max_length=100, unique=True, verbose_name='category name')),
                ('slug', models.SlugField(max_length=150)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='product.category', verbose_name='enter parent if exist')),
            ],
            options={
                'verbose_name_plural': 'categories',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_time_stamp', models.DateTimeField(blank=True, null=True, verbose_name='delete date')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('deleted', models.BooleanField(default=False, verbose_name='is deleted')),
                ('name', models.CharField(help_text='enter the discount', max_length=50, verbose_name='discount name')),
                ('discount', models.PositiveIntegerField(default=0, help_text='enter the discount', verbose_name='discount')),
                ('type', models.CharField(choices=[('percent', 'percent'), ('amount', 'amount')], max_length=50, verbose_name='type of discount')),
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
                ('deleted', models.BooleanField(default=False, verbose_name='is deleted')),
                ('name', models.CharField(help_text='enter name for discount', max_length=50, verbose_name='discount code')),
                ('code', models.IntegerField(help_text=' enter code for discount ', unique=True, verbose_name='discount code')),
                ('type', models.CharField(max_length=50, verbose_name='type of discountcode')),
                ('max_discount', models.PositiveIntegerField(help_text='please enter the max discount', verbose_name='maximum discount')),
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
                ('deleted', models.BooleanField(default=False, verbose_name='is deleted')),
                ('price', models.PositiveIntegerField(help_text='enter the price', verbose_name='price')),
                ('unit', models.CharField(choices=[('toman', 'toman'), ('dollar', 'dollar')], max_length=50, verbose_name='unit of money')),
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
                ('deleted', models.BooleanField(default=False, verbose_name='is deleted')),
                ('main_image', models.FileField(help_text='put picture for product', upload_to=product.models.product_image_path, verbose_name='image')),
                ('name', models.CharField(help_text='enter product name', max_length=200, verbose_name='name')),
                ('inventory', models.PositiveIntegerField(verbose_name='Inventory')),
                ('view', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='view')),
                ('inavailable', models.BooleanField(default=False, verbose_name='inavailable')),
                ('score', models.PositiveIntegerField(default=0, verbose_name='customer score')),
                ('slug', models.SlugField(max_length=150)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.brand', verbose_name='barnd name')),
                ('category', models.ForeignKey(help_text='enter the category', on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='category')),
                ('discount', models.ForeignKey(help_text='enter the discount', on_delete=django.db.models.deletion.CASCADE, to='product.discount', verbose_name='discount')),
                ('favourite', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.favourite', verbose_name='favourite product')),
                ('price', models.ForeignKey(help_text='enter the price', on_delete=django.db.models.deletion.CASCADE, to='product.price', verbose_name='price')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_time_stamp', models.DateTimeField(blank=True, null=True, verbose_name='delete date')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('deleted', models.BooleanField(default=False, verbose_name='is deleted')),
                ('image', models.FileField(help_text='put picture for product', upload_to=product.models.product_image_path, verbose_name='image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.product', verbose_name='product image')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
