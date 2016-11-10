from django import forms
from App.models import Fabric, Order, Customer, Address, Pattern_Piece, Style, Variation, Product, Notion, Log_Entry, Season, Collaborator, Collection, LabelTag, Size

class FabricForm(forms.ModelForm):
	class Meta:
		model = models.Fabric
		fields = [
			"title",
			"code",
			"content",
			"description",
			"quantity",
			"last_updated"
		]
class OrderForm(forms.ModelForm):
	class Meta:
		model = models.Order
		fields = [
			"order_date",
			"order_number",
			"originated_From",
			"order_status",
			"customer_id"
		]

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = [
			"address_id",
			"phone_number",
			"email",
			"name"
		]
class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields = [
			"street_number",
			"street_name",
			"city",
			"state",
			"zip_code"
		]
class PatternPieceForm(forms.ModelForm):
	class Meta:
		model = Pattern_Piece
		fields = [
			"title"
		]
class StyleForm(forms.ModelForm):
	class Meta:
		model = Style
		fields = [
			"title",
			"pattern_pieces",
			"code"
		]
class VariationForm(forms.ModelForm):
	class Meta:
		model = Variation
		fields = [
			"title",
			"pattern_pieces",
			"code"
		]
class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
			"SKU",
			"title",
			"description",
			"image_path",
			"tech_pack_path",
			"quantity",
			"collection_id",
			"style_id",
			"variation_id"
		]
class NotionForm(forms.ModelForm):
	class Meta:
		model = Notion
		fields = [
			"title",
			"description",
			"quantity",
			"last_updated"
		]
class LogEntryForm(forms.ModelForm):
	class Meta:
		model = Log_Entry
		fields = [
			"entry_date",
			"event"
		]
class SeasonForm(forms.ModelForm):
	class Meta:
		model = Season
		fields = [
			"title"
		]
class CollectionForm(forms.ModelForm):
	class Meta:
		model = Collection
		fields = [
			"title",
			"month",
			"code",
			"season_id",
		]
class CollaboratorForm(forms.ModelForm):
	class Meta:
		model = Collaborator
		fields = [
			"name"
		]
class LabelTagForm(forms.ModelForm):
	class Meta:
		model = LabelTag
		fields = [
			"title",
			"description",
			"quantity",
			"last_updated"
		]
class SizeForm(forms.ModelForm):
	class Meta:
		model = Size
		fields = [
			"size",
			"code"
		]
