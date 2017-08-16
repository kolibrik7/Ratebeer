from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models.functions import Lower
from django.contrib.auth.models import User

from .models import Brewery, Beer, Rating
from .forms import BeerForm

def zoznam(request):
	"""
	order_by = request.GET.get('order_by')
	if order_by:
		ordering = Lower(order_by)
	else:
		ordering = "id"
	"""
	beer_rating_list = Rating.objects.all()

	paginator = Paginator(beer_rating_list, 10)
	page = request.GET.get('page', 1)
	try:
		beers = paginator.page(page)
	except PageNotAnInteger:
		beers = paginator.page(1)
	except EmptyPage:
		beers = paginator.page(paginator.num_pages)

	return render(request, "beers/zoznam.html", {'beers': beers})

def pridanie_hodnotenia(request):
	if request.method == "POST":
		form = BeerForm(request.POST)
		if form.is_valid():
			obj_brewery = Brewery.objects.filter(brewery_name=request.POST["brewery"]).first()
			if not obj_brewery:
				obj_brewery = Brewery()
				obj_brewery.brewery_name = request.POST["brewery"]
				obj_brewery.country = request.POST["country"]
				obj_brewery.brewery_city = request.POST["brewery_city"]
				obj_brewery.save()

			obj_beer = Beer.objects.filter(pk=obj_brewery.id, beer_name=request.POST["beer_name"]).first()
			if not obj_beer:
				obj_beer = Beer()
				obj_beer.brewery = obj_brewery
				obj_beer.beer_name = request.POST["beer_name"]
				obj_beer.style = request.POST["style"]
				obj_beer.plato = request.POST["plato"]
				obj_beer.abv = request.POST["abv"]
				obj_beer.save()

			obj_rating = Rating()
			obj_rating.beer = obj_beer
			obj_rating.user = get_object_or_404(User, pk=request.POST["user_id"])
			obj_rating.city = request.POST["city"]
			obj_rating.place = request.POST["place"]
			obj_rating.date = form.cleaned_data["date"]
			obj_rating.serving = request.POST["serving"]
			obj_rating.price = request.POST["price"]
			obj_rating.volume = request.POST["volume"]
			obj_rating.rating = request.POST["rating"]
			obj_rating.note = request.POST["note"]
			obj_rating.save()

			return HttpResponseRedirect("/beers/pridanie_hodnotenia/")
	else:
		form = BeerForm()

	return render(request, "beers/pridanie_piva.html", {'form': form})

def uprava_hodnotenia(request, rating_id):
	beer = get_object_or_404(Beer, id=rating_id)
	form = BeerForm(request.POST or None, instance=beer)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/beers/")

	return render(request, "beers/editovanie_piva.html", {'form': form})

def detail(request, rating_id):
	rating = get_object_or_404(Rating, pk=rating_id)

	return render(request, "beers/detail.html", {'beer': beer})
