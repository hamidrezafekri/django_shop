# Generated by Django 3.2.6 on 2021-08-04 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_time_stamp', models.DateTimeField(blank=True, null=True, verbose_name='delete date')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='is deleted')),
                ('status', models.CharField(help_text='enter the order status', max_length=50, verbose_name='status')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reciept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_time_stamp', models.DateTimeField(blank=True, null=True, verbose_name='delete date')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='is deleted')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer', verbose_name='customer')),
                ('discountcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.discountcode', verbose_name='discount code')),
                ('orderstatus', models.ForeignKey(help_text='enter the status', on_delete=django.db.models.deletion.CASCADE, to='order.orderstatus', verbose_name='order status')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_time_stamp', models.DateTimeField(blank=True, null=True, verbose_name='delete date')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='is deleted')),
                ('favourite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.favourite')),
                ('product', models.ForeignKey(help_text='choose a product', on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_time_stamp', models.DateTimeField(blank=True, null=True, verbose_name='delete date')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='is deleted')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='quantity')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer', verbose_name='customer')),
                ('orderitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.orderitem', verbose_name='add order')),
                ('reciept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.reciept')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
