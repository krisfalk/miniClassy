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
	Log_Entry, Log_EntryAdmin, 
	Notion, NotionAdmin, 
	Pattern_Piece, Pattern_PieceAdmin, 
	Season, SeasonAdmin, 
	Style, StyleAdmin, 
	Variation, VariationAdmin, 
	Size, SizeAdmin
	)

# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Collaborator, CollaboratorAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Fabric, FabricAdmin)
admin.site.register(LabelTag, LabelTagAdmin)
admin.site.register(Log_Entry, Log_EntryAdmin)
admin.site.register(Notion, NotionAdmin)
admin.site.register(Pattern_Piece, Pattern_PieceAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Variation, VariationAdmin)