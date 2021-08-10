# Generated by Django 3.2.6 on 2021-08-09 23:33

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
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_time_stamp', models.DateTimeField(blank=True, null=True, verbose_name='delete date')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('deleted', models.BooleanField(default=False, verbose_name='is deleted')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer', verbose_name='customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_time_stamp', models.DateTimeField(blank=True, null=True, verbose_name='delete date')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('deleted', models.BooleanField(default=False, verbose_name='is deleted')),
                ('status', models.CharField(choices=[('processing', 'processing'), ('delivered', 'delivered'), ('cancled', 'cancled')], help_text='enter the order status', max_length=50, verbose_name='status')),
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
                ('deleted', models.BooleanField(default=False, verbose_name='is deleted')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='order quantity')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='add order')),
                ('product', models.ForeignKey(help_text='choose a product', on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.orderstatus'),
        ),
    ]
