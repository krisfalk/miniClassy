from django.shortcuts import render

# Create your views here.
from App.models import Product
from django.template import Context, loader
from django.shortcuts import render_to_response

def product(request):
	list_product = Product.objects.all()
	return render_to_response(
		'product.html',
		{'list_product': list_product}
	)