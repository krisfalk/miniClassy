from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from App.models  import LabelTag
from App.apps import genericFormLoader
from App.forms import LabelTagForm
# Create your views here.
def post_create(request):
	form = LabelTagForm(request.POST or None)
	#ADD FROM HERE
	LabelTagList = []
	for field in LabelTag._meta.fields:
		temp = field.get_attname_column()[0]
		LabelTagList.append(temp)

	string = genericFormLoader(LabelTagList)
	context = { "form": form, "string": string }
	#ADD TO HERE

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect('/LabelTag/create')
	else:
		form = LabelTagForm()

	return render(request, "create.html", context)

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
