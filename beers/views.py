from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models.functions import Lower

from .models import Beer
from .forms import BeerForm

def zoznam(request):
	order_by = request.GET.get('order_by')
	if order_by:
		ordering = Lower(order_by)
	else:
		ordering = "id"

	beer_list = Beer.objects.all().order_by(ordering)

	paginator = Paginator(beer_list, 10)
	page = request.GET.get('page', 1)
	try:
		beers = paginator.page(page)
	except PageNotAnInteger:
		beers = paginator.page(1)
	except EmptyPage:
		beers = paginator.page(paginator.num_pages)

	return render(request, "beers/zoznam.html", {'beers': beers, 'order_by': order_by})

def pridanie_hodnotenia(request):
	if request.method == "POST":
		form = BeerForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/beers/pridanie_hodnotenia/")
	else:
		form = BeerForm()

	return render(request, "beers/pridanie_piva.html", {'form': form})

def uprava_hodnotenia(request, beer_id):
	beer = get_object_or_404(Beer, id=beer_id)
	form = BeerForm(request.POST or None, instance=beer)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/beers/")

	return render(request, "beers/editovanie_piva.html", {'form': form})

def detail(request, beer_id):
	beer = get_object_or_404(Beer, pk=beer_id)
	return render(request, "beers/detail.html", {'beer': beer})
