# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 16:02
from __future__ import unicode_literals

import App.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collaborator_collection',
            name='collaborator_id',
        ),
        migrations.RemoveField(
            model_name='collaborator_collection',
            name='collection_id',
        ),
        migrations.RemoveField(
            model_name='fabric_product',
            name='fabric_id',
        ),
        migrations.RemoveField(
            model_name='fabric_product',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='labeltag_product',
            name='labelTag_id',
        ),
        migrations.RemoveField(
            model_name='labeltag_product',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='notion_product',
            name='notion_id',
        ),
        migrations.RemoveField(
            model_name='notion_product',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='order_sku',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='order_sku',
            name='product_id',
        ),
        migrations.AddField(
            model_name='collection',
            name='collaborator',
            field=models.ManyToManyField(to='App.Collaborator'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='App.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='fabric',
            field=models.ManyToManyField(to='App.Fabric'),
        ),
        migrations.AddField(
            model_name='product',
            name='label_tag',
            field=models.ManyToManyField(to='App.LabelTag'),
        ),
        migrations.AddField(
            model_name='product',
            name='notion',
            field=models.ManyToManyField(to='App.Notion'),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=100, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=50, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_name',
            field=models.CharField(max_length=100, verbose_name='Street Name'),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_number',
            field=models.IntegerField(verbose_name='Street Number'),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.IntegerField(verbose_name='Zip Code'),
        ),
        migrations.AlterField(
            model_name='collaborator',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='code',
            field=models.CharField(max_length=200, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='month',
            field=models.CharField(max_length=200, verbose_name='Month'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=50, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='fabric',
            name='code',
            field=models.CharField(max_length=200, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='fabric',
            name='content',
            field=models.CharField(max_length=200, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='fabric',
            name='description',
            field=models.CharField(max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='fabric',
            name='last_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Last Updated'),
        ),
        migrations.AlterField(
            model_name='fabric',
            name='quantity',
            field=models.FloatField(verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='fabric',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='labeltag',
            name='description',
            field=models.CharField(max_length=500, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='labeltag',
            name='last_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Last Updated'),
        ),
        migrations.AlterField(
            model_name='labeltag',
            name='quantity',
            field=models.IntegerField(verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='labeltag',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='log_entry',
            name='entry_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Entry Date'),
        ),
        migrations.AlterField(
            model_name='log_entry',
            name='event',
            field=models.CharField(max_length=200, verbose_name='Event'),
        ),
        migrations.AlterField(
            model_name='notion',
            name='description',
            field=models.CharField(max_length=500, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='notion',
            name='last_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Last Update'),
        ),
        migrations.AlterField(
            model_name='notion',
            name='quantity',
            field=models.IntegerField(verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='notion',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Order Date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.IntegerField(verbose_name='Order Number'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(verbose_name='Order Status'),
        ),
        migrations.AlterField(
            model_name='order',
            name='originated_From',
            field=models.CharField(max_length=200, verbose_name='Originated From'),
        ),
        migrations.AlterField(
            model_name='pattern_piece',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=500, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_path',
            field=models.FileField(upload_to=App.models.get_upload_file_name),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.FloatField(verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=200, verbose_name='SKU'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tech_pack_path',
            field=models.FileField(upload_to=App.models.get_upload_file_name),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='season',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='size',
            name='code',
            field=models.CharField(max_length=200, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(max_length=200, verbose_name='Size'),
        ),
        migrations.AlterField(
            model_name='style',
            name='code',
            field=models.CharField(max_length=200, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='style',
            name='pattern_pieces',
            field=models.CharField(max_length=200, verbose_name='Pattern Pieces'),
        ),
        migrations.AlterField(
            model_name='style',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='code',
            field=models.CharField(max_length=200, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='pattern_pieces',
            field=models.CharField(max_length=200, verbose_name='Pattern Pieces'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.DeleteModel(
            name='Collaborator_Collection',
        ),
        migrations.DeleteModel(
            name='Fabric_Product',
        ),
        migrations.DeleteModel(
            name='LabelTag_Product',
        ),
        migrations.DeleteModel(
            name='Notion_Product',
        ),
        migrations.DeleteModel(
            name='Order_Sku',
        ),
    ]
