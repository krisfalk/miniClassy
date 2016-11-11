from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from App.models  import Address
from App.apps import genericFormLoader
from App.forms import AddressForm
# Create your views here.
def post_create(request):
	form = AddressForm(request.POST or None)
	addressList = []
	for field in Address._meta.fields:
		temp = field.get_attname_column()[0]
		addressList.append(temp)

	string = genericFormLoader(addressList)
	context = { "form": form, "string": string }

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect('/address/create')
	else:
		form = AddressForm()

	return render(request, "create.html", context)

def post_detail(request, id):
	instance = get_object_or_404(Address, id=id)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return reender(request, "post_detail.html", context)

def post_list(request):
	if request.user.is_authenticated():
		context = {
			"title": "My User List"
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
