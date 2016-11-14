from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from App.models  import Product
from App.apps import genericFormLoader
from App.forms import ProductForm
from django.forms.models import model_to_dict
from django.core import serializers
# Create your views here.
def post_create(request):
	form = ProductForm(request.POST or None)
		#ADD FROM HERE
	productList = []
	for field in Product._meta.fields:
		temp = field.get_attname_column()[0]
		productList.append(temp)

	string = genericFormLoader(productList)
	context = { "form": form, "string": string }
		#ADD TO HERE

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect('/product/create')
	else:
		form = ProductForm()

		return render(request, "create.html", context)

def post_detail(request, id):
	instance = get_object_or_404(Product, id=id)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	form = ProductForm(None)
	data = serializers.serialize("python", Product.objects.all()),#whatever else)) #can add ,fields=('name','size')
	productList = []
	for field in Product._meta.fields:
		temp = field.get_attname_column()[0]
		productList.append(temp);

	if request.user.is_authenticated():
		context = {
			"form": form, "list": productList, "data": data,
		}
	else:
		context = {
			"title": "List"
		}
	return render(request, "index.html", context)
	#return HttpResponse("<h1>List</h1>")

def post_update(request):
	return HttpResponse("<h1>Update</h1>")

def post_delete(request):
	return HttpResponse("<h1>Delete</h1>")
