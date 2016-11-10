from django.shortcuts import render

# Create your views here.
from App.models import Product, Fabric
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm
from django.http import HttpResponseRedirect

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
