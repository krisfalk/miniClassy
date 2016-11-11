from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from App.models  import Size
from App.forms import SizeForm
from App.apps import genericFormLoader

def post_create(request):
	form = SizeForm(request.POST or None)
	#ADD FROM HERE
	sizeList = []
	for field in Size._meta.fields:
		temp = field.get_attname_column()[0]
		sizeList.append(temp)

	string = genericFormLoader(sizeList)
	context = { "form": form, "string": string }
	#ADD TO HERE

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect('/size/create')
	else:
		form = SizeForm()

	return render(request, "create.html", context)

def post_detail(request, id):
	instance = get_object_or_404(Size, id=id)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "post_detail.html", context)

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
