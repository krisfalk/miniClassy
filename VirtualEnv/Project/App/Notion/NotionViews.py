from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from App.models  import Notion
from App.apps import genericFormLoader
from App.forms import NotionForm
# Create your views here.
def post_create(request):
	form = NotionForm(request.POST or None)
	#ADD FROM HERE
	NotionList = []
	for field in Notion._meta.fields:
		temp = field.get_attname_column()[0]
		NotionList.append(temp)

	string = genericFormLoader(NotionList)
	context = { "form": form, "string": string }
	#ADD TO HERE

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect('/Notion/create')
	else:
		form = NotionForm()

	return render(request, "create.html", context)

def post_detail(request, id):
	instance = get_object_or_404(Notion, id=id)
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
