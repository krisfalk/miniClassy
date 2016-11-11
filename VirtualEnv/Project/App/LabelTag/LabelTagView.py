from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from App.models  import LabelTag
from App.forms import LabelTagForm
# Create your views here.
def post_create(request):
	form = LabelTagForm(request.POST or None)
	title = LabelTag.title
	description = LabelTag.description
	quantity = LabelTag.quantity
	last_updated = LabelTag.last_updated
	value = LabelTag

	context = {"form": form, "title": title, "description": description, "quantity": quantity, "last_updated": last_updated, "value": value}
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect('/labeltag')
	return render(request, "creates.html", context)

def post_detail(request, id):
	instance = get_object_or_404(LabelTag, id=id)
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