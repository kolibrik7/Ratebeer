from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Beer
from .forms import BeerForm

def zoznam(request):
	beer_list = Beer.objects.all()
	return render(request, "beers/zoznam.html", {'beer_list': beer_list})

def pridanie_piva(request):
	if request.method == "POST":
		form = BeerForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/beers/")
	else:
		form = BeerForm()

	return render(request, "beers/pridanie_piva.html", {'form': form})

def detail(request, beer_id):
	beer = get_object_or_404(Beer, pk=beer_id)
	return render(request, "beers/detail.html", {'beer': beer})
