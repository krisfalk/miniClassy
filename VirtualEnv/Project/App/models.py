from django.db import models
from datetime import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.contrib import admin

from time import time

# Create your models here.
def get_upload_file_name(instance, filename):
    return "uploaded_files/%s" % (filename)

class LabelTag(models.Model):
    title = models.CharField("Title", max_length = 200)
    description = models.CharField("Description", max_length = 500)
    quantity = models.IntegerField("Quantity")
    last_updated = models.DateTimeField("Last Updated", default=datetime.now, blank=True)
    def __str__(self):
        return '%s %s %s %s' % (self.title, self.description, self.quantity, self.last_updated)

class LabelTagAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'quantity', 'last_updated')
    list_display_links = ('title', 'description', 'quantity', 'last_updated')
    list_filter = ('title', 'description', 'last_updated')
    ordering = ['title', 'last_updated']
    search_fields = ('title', 'description', 'last_updated')
    list_per_page = 25

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='EditQuantity'):
            return ('title', 'description', 'last_updated')
        else:
            return (super(LabelTagAdmin, self).get_readonly_fields(request, obj))

class Fabric(models.Model):
    title = models.CharField("Title", max_length = 200)
    code = models.CharField("Code", max_length = 200)
    content = models.CharField("Content", max_length = 200)
    description = models.CharField("Description", max_length = 200)
    quantity = models.FloatField("Quantity")
    last_updated = models.DateTimeField("Last Updated", default=datetime.now, blank=True)
    def __str__(self):
        return '%s %s %s %s %s %s' % (self.title, self.code, self.content, self.description, self.quantity, self.last_updated)

class FabricAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'content', 'description', 'quantity', 'last_updated')
    list_display_links = ('title', 'code', 'content', 'description', 'quantity', 'last_updated')
    list_filter = ('title', 'code', 'content', 'description', 'last_updated')
    ordering = ['title']
    search_fields = ('title', 'code', 'content', 'description', 'last_updated')
    list_per_page = 25


    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='EditQuantity'):
            return ('title', 'code', 'content', 'description', 'last_updated')
        else:
            return (super(FabricAdmin, self).get_readonly_fields(request, obj))

class Customer(models.Model):
    address_id = models.ForeignKey('Address')
    #address_shipping_id = models.ForeignKey('Address', related_name="shipping")
    phone_number = models.CharField("Phone Number", max_length = 15)
    email = models.CharField("Email", max_length = 50)
    name = models.CharField("Name", max_length = 100)
    def __str__(self):
        return '%s %s %s %s' % (self.address_id, self.phone_number, self.email, self.name)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('address_id', 'phone_number', 'email', 'name')
    list_display_links = ('address_id', 'phone_number', 'email', 'name')
    list_filter = ('address_id', 'phone_number', 'email', 'name')
    ordering = ['name']
    search_fields = ('address_id', 'phone_number', 'email', 'name')
    list_per_page = 25

class Address(models.Model):
    street_number = models.IntegerField("Street Number")
    street_name = models.CharField("Street Name", max_length = 100)
    city = models.CharField("City", max_length = 100)
    state = models.CharField("State", max_length = 50)
    zip_code = models.IntegerField("Zip Code")
    def __str__(self):
        return '%s %s %s %s %s' % (self.street_number, self.street_name, self.city, self.state, self.zip_code)

class AddressAdmin(admin.ModelAdmin):
    list_display = ('street_number', 'street_name', 'city', 'state', 'zip_code')
    list_display_links = ('street_number', 'street_name', 'city', 'state', 'zip_code')
    list_filter = ('street_number', 'street_name', 'city', 'state', 'zip_code')
    ordering = ['zip_code', 'street_name', 'street_number']
    search_fields = ('street_number', 'street_name', 'city', 'state', 'zip_code')
    list_per_page = 25

class Pattern_Piece(models.Model):
    title = models.CharField("Title", max_length = 100)
    def __str__(self):
        return self.title

class Pattern_PieceAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )
    list_filter = ('title', )
    ordering = ['title']
    search_fields = ('title', )
    list_per_page = 25

class Style(models.Model):
    title = models.CharField("Title", max_length = 100)
    #pattern_pieces is a string, but will be a list of ints
    #separated by a ','. Example: "1,2,3"
    #When adding to this string, add a ',' then the new number
    #Example: pattern_pieces += "," + newValue
    pattern_pieces = models.ManyToManyField(Pattern_Piece)
    code = models.CharField("Code", max_length = 200)
    def __str__(self):
        return '%s %s' % (self.title, self.code)

class StyleAdmin(admin.ModelAdmin):
    list_display = ('title', 'code')
    list_display_links = ('title', 'code')
    list_filter = ('title', 'code')
    ordering = ['title']
    search_fields = ('title', 'code')
    list_per_page = 25

class Variation(models.Model):
    title = models.CharField("Title", max_length = 100)
    pattern_pieces = models.ManyToManyField('Pattern_Piece')
    code = models.CharField("Code", max_length = 200)
    def __str__(self):
        return '%s %s' % (self.title, self.code)

class VariationAdmin(admin.ModelAdmin):
    list_display = ('title', 'code')
    list_display_links = ('title', 'code')
    list_filter = ('title', 'code')
    ordering = ['title']
    search_fields = ('title', 'code')
    list_per_page = 25

class Notion(models.Model):
    title = models.CharField("Title", max_length = 100)
    description = models.CharField("Description", max_length = 500)
    quantity = models.IntegerField("Quantity")
    last_updated = models.DateTimeField("Last Update", default=datetime.now, blank=True)
    def __str__(self):
        return '%s %s %s %s' % (self.title, self.description, self.quantity, self.last_updated)

class NotionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'quantity', 'last_updated')
    list_display_links = ('title', 'description', 'quantity', 'last_updated')
    list_filter = ('title', 'description', 'last_updated')
    ordering = ['title']
    search_fields = ('title', 'description', 'last_updated')
    list_per_page = 25

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='EditQuantity'):
            return ('title', 'description', 'last_updated')
        else:
            return (super(NotionAdmin, self).get_readonly_fields(request, obj))

class Product_Notion_Quantity(models.Model):
    notion = models.ForeignKey('Notion')
    quantity = models.IntegerField("Quantity")
    def __str__(self):
        return '%s %s' % (self.notion, self.quantity)

class Product_Notion_QuantityAdmin(admin.ModelAdmin):
    list_display = ('notion', 'quantity')
    list_display_links = ('notion', 'quantity')
    list_filter = ('notion', 'quantity')
    ordering = ['notion', 'quantity']
    search_fields = ('notion', 'quantity')
    list_per_page = 25

    def get_model_perms(self, request):
        return {}

class Product_Fabric_Quantity(models.Model):
    fabric = models.ForeignKey('Fabric')
    quantity = models.IntegerField("Quantity")
    def __str__(self):
        return '%s %s' % (self.fabric, self.quantity)

class Product_Fabric_QuantityAdmin(admin.ModelAdmin):
    list_display = ('fabric', 'quantity')
    list_display_links = ('fabric', 'quantity')
    list_filter = ('fabric', 'quantity')
    ordering = ['fabric', 'quantity']
    search_fields = ('fabric', 'quantity')
    list_per_page = 25

    def get_model_perms(self, request):
        return {}

class Product(models.Model):
    sku = models.CharField("SKU", max_length = 200)
    title = models.CharField("Title", max_length = 200)
    description = models.CharField("Description", max_length = 500)
    image_path = models.FileField(upload_to=get_upload_file_name)
    tech_pack_path = models.FileField(upload_to=get_upload_file_name)
    quantity = models.FloatField("Quantity")
    collection_id = models.ForeignKey('Collection')
    style_id = models.ForeignKey('Style')
    variation_id = models.ForeignKey('Variation')
    notions = models.ManyToManyField(Product_Notion_Quantity)
    fabrics = models.ManyToManyField(Product_Fabric_Quantity)
    label_tag = models.ManyToManyField(LabelTag)
    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s' % (self.sku, self.title, self.description, self.image_path, self.tech_pack_path, self.quantity, self.collection_id, self.style_id, self.variation_id)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'title', 'description', 'image_path', 'tech_pack_path', 'quantity', 'collection_id', 'style_id', 'variation_id')
    list_display_links = ('sku', 'title', 'description', 'image_path', 'tech_pack_path', 'quantity', 'collection_id', 'style_id', 'variation_id')
    list_filter = ('sku', 'title', 'description', 'image_path', 'tech_pack_path', 'collection_id', 'style_id', 'variation_id')
    ordering = ['sku']
    search_fields = ('sku', 'title', 'description', 'image_path', 'tech_pack_path', 'collection_id', 'style_id', 'variation_id')
    list_per_page = 25

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='EditQuantity'):
            return ('sku', 'title', 'description', 'image_path', 'tech_pack_path', 'collection_id', 'style_id', 'variation_id')
        else:
            return (super(ProductAdmin, self).get_readonly_fields(request, obj))



class Class_Type(models.Model):
    title = models.CharField("Title", max_length = 200)
    def __str__(self):
        return '%s' % (self.title)

class Class_TypeAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )
    list_filter = ('title', )
    ordering = ['title']
    search_fields = ('title', )
    list_per_page = 25

class Product_Quantity(models.Model):
    product_type = models.ForeignKey('Product')
    quantity = models.IntegerField("Quantity")
    class_type = models.ForeignKey('Class_Type')
    def __str__(self):
        return '%s' % (self.product_type)

class Product_QuantityAdmin(admin.ModelAdmin):
    list_display = ('product_type', 'quantity', 'class_type')
    list_display_links = ('product_type', 'quantity', 'class_type')
    list_filter = ('product_type', 'quantity', 'class_type')
    ordering = ['product_type', 'quantity', 'class_type']
    search_fields = ('product_type', 'quantity', 'class_type')
    list_per_page = 25

    def get_model_perms(self, request):
        return {}


class Order(models.Model):
    order_date = models.DateTimeField("Order Date", default=datetime.now, blank=True)
    order_number = models.IntegerField("Order Number")
    originated_From = models.CharField("Originated From", max_length = 200)
    order_status = models.IntegerField("Order Status")
    customer_id = models.ForeignKey('Customer')
    product = models.ManyToManyField(Product_Quantity)

    def __str__(self):
        return '%s %s %s %s %s' % (self.order_date, self.order_number, self.originated_From, self.order_status, self.customer_id)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_date', 'order_number', 'originated_From', 'order_status', 'customer_id')
    list_display_links = ('order_date', 'order_number', 'originated_From', 'order_status', 'customer_id')
    list_filter = ('order_date', 'order_number', 'originated_From', 'order_status', 'customer_id')
    ordering = ['order_date']
    search_fields = ('order_date', 'order_number', 'originated_From', 'order_status', 'customer_id')
    list_per_page = 25

class Log_Entry(models.Model):
    entry_date = models.DateTimeField("Entry Date", default=datetime.now, blank=True)
    event = models.CharField("Event", max_length = 200)
    def __str__(self):
        return '%s %s' % (self.entry_date, self.event)

class Log_EntryAdmin(admin.ModelAdmin):
    list_display = ('entry_date', 'event')
    list_display_links = ('entry_date', 'event')
    list_filter = ('entry_date', 'event')
    ordering = ['entry_date']
    search_fields = ('entry_date', 'event')
    list_per_page = 25

class Season(models.Model):
    title = models.CharField("Title", max_length = 200)
    def __str__(self):
        return self.title

class SeasonAdmin(admin.ModelAdmin):
   list_display = ('title', )
   list_display_links = ('title', )
   list_filter = ('title', )
   ordering = ['title']
   search_fields = ('title', )
   list_per_page = 25

class Collaborator(models.Model):
    name = models.CharField("Name", max_length = 200)
    def __str__(self):
        return self.name

class CollaboratorAdmin(admin.ModelAdmin):
   list_display = ('name', )
   list_display_links = ('name', )
   list_filter = ('name', )
   ordering = ['name']
   search_fields = ('name', )
   list_per_page = 25

class Collection(models.Model):
    title = models.CharField("Title", max_length = 200)
    month = models.CharField("Month", max_length = 200)
    code = models.CharField("Code", max_length = 200)
    season_id = models.ForeignKey('Season')
    collaborator = models.ManyToManyField(Collaborator)
    def __str__(self):
        return '%s %s %s %s' % (self.title, self.month, self.code, self.season_id)

class CollectionAdmin(admin.ModelAdmin):
   list_display = ('title', 'month', 'code', 'season_id')
   list_display_links = ('title', 'month', 'code', 'season_id')
   list_filter = ('title', 'month', 'code', 'season_id')
   ordering = ['title']
   search_fields = ('title', 'month', 'code', 'season_id')
   list_per_page = 25

class Size(models.Model):
    size = models.CharField("Size", max_length = 200)
    code = models.CharField("Code", max_length = 200)
    def __str__(self):
        return '%s %s' % (self.size, self.code)

class SizeAdmin(admin.ModelAdmin):
     list_display = ('size', 'code')
     list_display_links = ('size', 'code')
     list_filter = ('size', 'code')
     ordering = ['code']
     search_fields = ('size', 'code')
     list_per_page = 25




# class Collaborator_Collection(models.Model):
#     collection_id = models.ForeignKey('Collection')
#     collaborator_id = models.ForeignKey('Collaborator')
#     def __str__(self):
#         return '%s %s' % (self.collection_id, self.collaborator_id)

# class LabelTag_Product(models.Model):
#     labelTag_id = models.ForeignKey('LabelTag')
#     product_id = models.ForeignKey('Product')
#     def __str__(self):
#         return '%s %s' % (self.labelTag_id, self.product_id)


# class Order_Sku(models.Model):
#     order_id = models.ForeignKey('Order')
#     product_id = models.ForeignKey('Product')
#     def __str__(self):
#         return '%s %s' % (self.order_id, self.product_id)

# class Notion_Product(models.Model):
#     notion_id = models.ForeignKey('Notion')
#     product_id = models.ForeignKey('Product')
#     def __str__(self):
#         return '%s %s' % (self.notion_id, self.product_id)
# class Product_Notion(models.Model):
#     notion_id = models.ForeignKey('Notion')
#     product_id = models.ForeignKey('Product')
#     def __str__(self):
#         return '%s %s' % (self.notion_id, self.product_id)

# class Fabric_Product(models.Model):
#     fabric_id = models.ForeignKey('Fabric')
#     product_id = models.ForeignKey('Product')
#     def __str__(self):
#         return '%s %s' % (self.fabric_id, self.product_id)
