from django import forms
from .models import Fabric

class PostForm(forms.ModelForm):
	class Meta:
		model = Fabric
		fields = [
			"title",
			"code",
			"content",
			"description",
			"quantity",
			"last_updated"
		]
