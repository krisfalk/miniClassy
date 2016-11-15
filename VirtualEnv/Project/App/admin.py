from django.contrib import admin
from App.models import SizeAdmin, Order, Address, Collaborator, Collection, Customer, Product, Fabric, LabelTag, Log_Entry, Notion, Pattern_Piece, Season, Style, Variation, Size

# Register your models here.
admin.site.register(Order)
admin.site.register(Address)
admin.site.register(Collaborator)
admin.site.register(Collection)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Fabric)
admin.site.register(LabelTag)
admin.site.register(Log_Entry)
admin.site.register(Notion)
admin.site.register(Pattern_Piece)
admin.site.register(Season)
admin.site.register(Size, SizeAdmin)
admin.site.register(Style)
admin.site.register(Variation)