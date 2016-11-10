from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from App.models  import Style
# Create your views here.
def post_create(request):
	return HttpResponse("<h1>Create</h1>")

def post_detail(request, id):
	instance = get_object_or_404(Style, id=id)
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
	return reender(request, "index.html", context)
	#return HttpResponse("<h1>List</h1>")

def post_update(request):
	return HttpResponse("<h1>Update</h1>")

def post_delete(request):
	return HttpResponse("<h1>Delete</h1>")
