from django.db import models
from datetime import datetime
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

class Order(models.Model):
    order_date = models.DateTimeField("Order Date", default=datetime.now, blank=True)
    order_number = models.IntegerField("Order Number")
    originated_From = models.CharField("Originated From", max_length = 200)
    order_status = models.IntegerField("Order Status")
    customer_id = models.ForeignKey('Customer')
    def __str_(self):
        return '%s %s %s %s %s' % (self.order_date, self.order_number, self.originated_From, self.order_status, self.customer_id)


class Customer(models.Model):
    address_id = models.ForeignKey('Address')
    #address_shipping_id = models.ForeignKey('Address', related_name="shipping")
    phone_number = models.CharField("Phone Number", max_length = 15)
    email = models.CharField("Email", max_length = 50)
    name = models.CharField("Name", max_length = 100)
    def __str__(self):
        return '%s %s %s %s' % (self.address_id, self.phone_number, self.email, self.name)

class Address(models.Model):
    street_number = models.IntegerField("Street Number")
    street_name = models.CharField("Street Name", max_length = 100)
    city = models.CharField("City", max_length = 100)
    state = models.CharField("State", max_length = 50)
    zip_code = models.IntegerField("Zip Code")
    def __str__(self):
        return '%s %s %s %s %s' % (self.street_number, self.street_name, self.city, self.state, self.zip_code)

class Pattern_Piece(models.Model):
    title = models.CharField("Titel", max_length = 100)
    def __str__(self):
        return self.title

class Style(models.Model):
    title = models.CharField("Title", max_length = 100)
    #pattern_pieces is a string, but will be a list of ints
    #separated by a ','. Example: "1,2,3"
    #When adding to this string, add a ',' then the new number
    #Example: pattern_pieces += "," + newValue
    pattern_pieces = models.CharField("Pattern Pieces", max_length = 200)
    code = models.CharField("Code", max_length = 200)
    def __str__(self):
        return '%s %s %s' % (self.title, self.pattern_pieces, self.code)

class Variation(models.Model):
    title = models.CharField("Title", max_length = 100)
    pattern_pieces = models.CharField("Pattern Pieces", max_length = 200)
    code = models.CharField("Code", max_length = 200)
    def __str__(self):
        return '%s %s %s' % (self.title, self.pattern_pieces, self.code)

class Product(models.Model):
    sku = models.CharField("SKU", max_length = 200)
    title = models.CharField("Title", max_length = 200)
    description = models.CharField("Description", max_length = 500)
    image_path = models.CharField("Image Path", max_length = 200)
    tech_pack_path = models.CharField("Tech Pack Path", max_length = 200)
    quantity = models.FloatField("Quantity")
    collection_id = models.ForeignKey('Collection')
    style_id = models.ForeignKey('Style')
    variation_id = models.ForeignKey('Variation')
    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s' % (self.sku, self.title, self.description, self.image_path, self.tech_pack_path, self.quantity, self.collection_id, self.style_id, self.variation_id)

class Order_Sku(models.Model):
    order_id = models.ForeignKey('Order')
    product_id = models.ForeignKey('Product')
    def __str__(self):
        return '%s %s' % (self.order_id, self.product_id)

class Notion_Product(models.Model):
    notion_id = models.ForeignKey('Notion')
    product_id = models.ForeignKey('Product')
    def __str__(self):
        return '%s %s' % (self.notion_id, self.product_id)

class Notion(models.Model):
    title = models.CharField("Title", max_length = 100)
    description = models.CharField("Description", max_length = 500)
    quantity = models.IntegerField("Quantity")
    last_updated = models.DateTimeField("Last Update", default=datetime.now, blank=True)
    def __str__(self):
        return '%s %s %s %s' % (self.title, self.description, self.quantity, self.last_updated)

class Fabric_Product(models.Model):
    fabric_id = models.ForeignKey('Fabric')
    product_id = models.ForeignKey('Product')
    def __str__(self):
        return '%s %s' % (self.fabric_id, self.product_id)

class Log_Entry(models.Model):
    entry_date = models.DateTimeField("Entry Date", default=datetime.now, blank=True)
    event = models.CharField("Event", max_length = 200)
    def __str__(self):
        return '%s %s' % (self.entry_date, self.event)

class Season(models.Model):
    title = models.CharField("Title", max_length = 200)
    def __str__(self):
        return self.title

class Collection(models.Model):
    title = models.CharField("Title", max_length = 200)
    month = models.CharField("Month", max_length = 200)
    code = models.CharField("Code", max_length = 200)
    season_id = models.ForeignKey('Season')
    def __str__(self):
        return '%s %s %s %s' % (self.title, self.month, self.code, self.season_id)

class Collaborator_Collection(models.Model):
    collection_id = models.ForeignKey('Collection')
    collaborator_id = models.ForeignKey('Collaborator')
    def __str__(self):
        return '%s %s' % (self.collection_id, self.collaborator_id)

class Collaborator(models.Model):
    name = models.CharField("Name", max_length = 200)
    def __str__(self):
        return self.name

class LabelTag_Product(models.Model):
    labelTag_id = models.ForeignKey('LabelTag')
    product_id = models.ForeignKey('Product')
    def __str__(self):
        return '%s %s' % (self.labelTag_id, self.product_id)

class LabelTag(models.Model):
    title = models.CharField("Title", max_length = 200)
    description = models.CharField("Description", max_length = 500)
    quantity = models.IntegerField("Quantity")
    last_updated = models.DateTimeField("Last Updated", default=datetime.now, blank=True)
    def __str__(self):
        return '%s %s %s %s' (self.title, self.description, self.quantity, self.last_updated)

class Fabric(models.Model):
    title = models.CharField("Title", max_length = 200)
    code = models.CharField("Code", max_length = 200)
    content = models.CharField("Content", max_length = 200)
    description = models.CharField("Description", max_length = 200)
    quantity = models.FloatField("Quantity")
    last_updated = models.DateTimeField("Last Updated", default=datetime.now, blank=True)
    def __str__(self):
        return '%s %s %s %s %s %s' % (self.title, self.code, self.content, self.description, self.quantity, self.last_updated)

class Size(models.Model):
    size = models.CharField("Size", max_length = 200)
    code = models.CharField("Code", max_length = 200)
    def __str__(self):
        return '%s %s' % (self.size, self.code)
