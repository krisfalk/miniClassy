from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from App.models  import Collection
from App.apps import genericFormLoader
from App.forms import CollectionForm
# Create your views here.
def post_create(request):
	form = CollectionForm(request.POST or None)
	collectionList = []
	for field in Collection._meta.fields:
		temp = field.get_attname_column()[0]
		collectionList.append(temp)

	string = genericFormLoader(collectionList)
	context = { "form": form, "string": string }

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect('/collection/create')
	else:
		form = CollectionForm()

		return render(request, "create.html", context)

def post_detail(request, id):
	instance = get_object_or_404(Collection, id=id)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	if request.user.is_authenticated():
		Collection.objects.all()

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
