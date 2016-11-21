from django.contrib import admin
from App.models import (
	Order, OrderAdmin,
	Address, AddressAdmin,
	Collaborator, CollaboratorAdmin,
	Collection, CollectionAdmin,
	Customer, CustomerAdmin,
	Product, ProductAdmin,
	Fabric, FabricAdmin,
	LabelTag, LabelTagAdmin,
	#Log_Entry, Log_EntryAdmin,
	Notion, NotionAdmin,
	Pattern_Piece, Pattern_PieceAdmin,
	Season, SeasonAdmin,
	Style, StyleAdmin,
	Variation, VariationAdmin,
	Size, SizeAdmin,
	Product_Quantity, Product_QuantityAdmin,
	Product_Notion_Quantity, Product_Notion_QuantityAdmin,
	Product_Fabric_Quantity, Product_Fabric_QuantityAdmin,
	Class_Type, Class_TypeAdmin,
	Product_LabelTag_Quantity, Product_LabelTag_QuantityAdmin,
	LogEntryAdmin)
from django.contrib.admin.models import LogEntry

# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Collaborator, CollaboratorAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Fabric, FabricAdmin)
admin.site.register(LabelTag, LabelTagAdmin)
#admin.site.register(Log_Entry, Log_EntryAdmin)
admin.site.register(Notion, NotionAdmin)
admin.site.register(Pattern_Piece, Pattern_PieceAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(Product_Quantity, Product_QuantityAdmin)
admin.site.register(Product_Notion_Quantity, Product_Notion_QuantityAdmin)
admin.site.register(Product_Fabric_Quantity, Product_Fabric_QuantityAdmin)
admin.site.register(Product_LabelTag_Quantity, Product_LabelTag_QuantityAdmin)
admin.site.register(Class_Type, Class_TypeAdmin)
admin.site.register(LogEntry, LogEntryAdmin)

admin.site.disable_action('delete_selected')