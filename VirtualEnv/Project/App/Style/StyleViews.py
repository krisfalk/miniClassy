from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from App.models  import Style
from App.apps import genericFormLoader
from App.forms import StyleForm
# Create your views here.
def post_create(request):
	form = StyleForm(request.POST or None)
#ADD FROM HERE
	styleList = []
	for field in Style._meta.fields:
		temp = field.get_attname_column()[0]
		styleList.append(temp)

	string = genericFormLoader(styleList)
	context = { "form": form, "string": string }
#ADD TO HERE

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect('/style/create')
	else:
		form = StyleForm()

		return render(request, "create.html", context)


# def product(request):
#
# 	fabrics = Fabric.objects.all()
# 	list_fabric_pages = Paginator(fabrics, 3)
# 	page = request.GET.get('page')
#
# 	try:
# 		list_fabric = list_fabric_pages.page(page)
# 	except PageNotAnInteger:
# 		list_fabric = list_fabric_pages.page(1)
# 	except EmptyPage:
# 		list_fabric = list_fabric_pages.page(list_fabric_pages.num_pages)
#
# 	return render_to_response('fabric.html', {'list_fabric': list_fabric})

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
