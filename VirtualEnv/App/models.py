from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

class Order(models.Model):
    order_date = models.DateTimeField(default=datetime.now, blank=True)
    order_number = models.IntegerField()
    originated_From = models.CharField(max_length = 200)
    order_status = models.IntegerField()
    customer_id = models.ForeignKey('Customer')

class Customer(models.Model):
    address_billing_id = models.ForeignKey('Address')
    address_shipping_id = models.ForeignKey('Address')
    phone_number = models.CharField(max_length = 15)
    email = models.CharField(max_length = 50)
    name = models.CharField(max_length = 100)

class Address(models.Model):
    street_number = models.IntegerField()
    street_name = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 50)
    zip_code = models.IntegerField()

class Pattern_Piece(models.Model):
    title = models.CharField(max_length = 100)

class Style(models.Model):
    title = models.CharField(max_length = 100)
    #pattern_pieces is a string, but will be a list of ints
    #separated by a ','. Example: "1,2,3"
    #When adding to this string, add a ',' then the new number
    #Example: pattern_pieces += "," + newValue
    pattern_pieces = models.CharField()
    code = models.CharField()

class Variation(models.Model):
    title = models.CharField(max_length = 100)
    pattern_pieces = models.CharField()
    code = models.CharField()

class Product(models.Model):
    sku = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)
    description = models.CharField()
    image_path = models.CharField()
    tech_pack_path = models.CharField()
    quantity = models.FloatField()
    collection_id = models.ForeignKey('Collection')
    style_id = models.ForeignKey('Style')
    variation_id = models.ForeignKey('Variation')

class Order_Sku(models.Model):
    order_id = models.ForeignKey('Order')
    product_id = models.ForeignKey('Product')

class Notion_Product(models.Model):
    notion_id = models.ForeignKey('Notion')
    product_id = models.ForeignKey('Product')

class Notion(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField()
    quantity = models.IntegerField()
    last_updated = models.DateTimeField(default=datetime.now, blank=True)

class Fabric_Product(models.Model):
    fabric_id = models.ForeignKey('Fabric')
    product_id = models.ForeignKey('Product')

class Log_Entry(models.Model):
    entry_date = models.DateTimeField(default=datetime.now, blank=True)
    event = models.CharField()

class Season(models.Model):
    title = models.CharField(max_length = 200)
    def __str__(self):
        return self.title

class Collection(models.Model):
    title = models.CharField('Title', max_length = 200)
    month = models.CharField('Month', max_length = 200)
    code = models.CharField('Code', max_length = 200)
    season_id = models.ForeignKey('Season')
    def __str__(self):
        return u'%s %s %s' % (self.title, self.month, self.code)

class Collaborator_Collection(models.Model):
    collection_id = models.ForeignKey('Collection')
    collaborator_id = models.ForeignKey('Collaborator')

class Collaborator(models.Model):
    name = models.CharField(max_length = 200)

class LabelTag_Product(models.Model):
    labelTag_id = models.ForeignKey('LabelTag')
    product_id = models.ForeignKey('Product')

class LabelTag(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField()
    quantity = models.IntegerField()
    last_updated = models.DateTimeField(default=datetime.now, blank=True)

class Fabric(models.Model):
    title = models.CharField(max_length = 200)
    code = models.CharField(max_length = 200)
    content = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    quantity = models.FloatField()
    last_updated = models.DateTimeField(default=datetime.now, blank=True)

class Size(models.Model):
    title = models.CharField('Title', max_length = 200)
    code = models.CharField('Code', max_length = 200)