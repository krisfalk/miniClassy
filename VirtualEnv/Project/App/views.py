from django.shortcuts import render

# Create your views here.
from App.models import Product, Fabric
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm
from django.http import HttpResponseRedirect
# def product(request):
# 	list_product = Product.objects.all()
# 	return render_to_response(
# 		'product.html',
# 		{'list_product': list_product}
# 	)

def product(request):

	products = Product.objects.all()
	list_product_pages = Paginator(products, 3)
	page = request.GET.get('page')

	try:
		list_product = list_product_pages.page(page)
	except PageNotAnInteger:
		list_product = list_product_pages.page(1)
	except EmptyPage:
		list_product = list_product_pages.page(list_product_pages.num_pages)

	return render_to_response('product.html', {'list_product': list_product})

# def new_product(request):
# 	return render_to_response(
# 		'form.html',
# 		{'action': 'add',
# 		'button': 'Add'}
# 	)

# def add_product(request):
# 	sku = request.POST["sku"]
# 	title = request.POST["title"]
# 	description = request.POST["description"]
# 	image_path = request.POST["image_path"]
# 	tech_pack_path = request.POST["tech_pack_path"]
# 	quantity = request.POST["quantity"]
# 	collection_id = request.POST["collection_id"]
# 	style_id = request.POST["style_id"]
# 	variation_id = request.POST["variation_id"]

# 	product = Product(
# 		sku = sku,
# 		title = title,
# 		description = description,
# 		image_path = image_path,
# 		tech_pack_path = tech_pack_path,
# 		quantity = quantity,
# 		collection_id = collection_id,
# 		style_id = style_id,
# 		variation_id = variation_id
# 		)
# 	product.save()

def product(request):

	fabrics = Fabric.objects.all()
	list_fabric_pages = Paginator(fabrics, 3)
	page = request.GET.get('page')

	try:
		list_fabric = list_fabric_pages.page(page)
	except PageNotAnInteger:
		list_fabric = list_fabric_pages.page(1)
	except EmptyPage:
		list_fabric = list_fabric_pages.page(list_fabric_pages.num_pages)

	return render_to_response('fabric.html', {'list_fabric': list_fabric})

def newProduct(request):

	form = PostForm(request.POST or None)
	context = { "form": form, }
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect('/fabric')
	else:
		form = PostForm()
	return render(request, "fabric_form.html", context)


# def add(request):
# 	title = request.POST["title"]
# 	description = request.POST["description"]
# 	code = request.POST["code"]
# 	content = request.POST["content"]
# 	quantity = request.POST["quantity"]

# 	fabric = Fabric(
# 		title = title,
# 		description = description,
# 		code = code,
# 		content = content,
# 		quantity = quantity
# 		)

# 	fabric.save()
