from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from App.models  import Pattern_Piece
from App.apps import genericFormLoader
from App.forms import PatternPieceForm
# Create your views here.
def post_create(request):
	form = PatternPieceForm(request.POST or None)
	#ADD FROM HERE
	patternPieceList = []
	for field in Pattern_Piece._meta.fields:
		temp = field.get_attname_column()[0]
		patternPieceList.append(temp)

	string = genericFormLoader(patternPieceList)
	context = { "form": form, "string": string }
	#ADD TO HERE

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect('/patternpiece/create')
	else:
		form = PatternPieceForm()

	return render(request, "create.html", context)

def post_detail(request, id):
	instance = get_object_or_404(Pattern_Piece, id=id)
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
