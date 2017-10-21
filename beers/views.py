from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models.functions import Lower
from django.contrib.auth.models import User

from .models import Brewery, Beer, Rating
from .forms import BeerForm

def zoznam(request):

	order_by = request.GET.get('order_by')
	if order_by:
		if order_by == "brewery":
			ordering = "beer__brewery__brewery_name"
		elif order_by == "beer":
			ordering = "beer__beer_name"
		elif order_by == "style":
			ordering = "beer__style"
		else:
			ordering = Lower(order_by)
	else:
		ordering = "date"
	
	beer_rating_list = Rating.objects.filter(user__id=request.user.id).select_related().order_by(ordering)

	paginator = Paginator(beer_rating_list, 30)
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
				plato = request.POST["plato"]
				if plato:
					obj_beer.plato = plato
				else:
					obj_beer.plato = None
				abv = request.POST["abv"]
				if abv:
					obj_beer.abv = abv
				else:
					obj_beer.abv = None
				obj_beer.save()

			obj_rating = Rating()
			obj_rating.beer = obj_beer
			obj_rating.user = get_object_or_404(User, pk=request.user.id)
			obj_rating.city = request.POST["city"]
			obj_rating.place = request.POST["place"]
			obj_rating.date = form.cleaned_data["date"]
			obj_rating.serving = request.POST["serving"]
			price = request.POST["price"]
			if price:
				obj_rating.price = price
			else:
				obj_rating.price = None
			obj_rating.volume = request.POST["volume"]
			obj_rating.rating = request.POST["rating"]
			obj_rating.note = request.POST["note"]
			obj_rating.save()

			return HttpResponseRedirect("/beers/pridanie_hodnotenia/")
	else:
		form = BeerForm()

	return render(request, "beers/pridanie_piva.html", {'form': form})

def uprava_hodnotenia(request, rating_id):
	rating = Rating.objects.filter(pk=rating_id, user__id=request.user.id).select_related().first()

	context = {
		'brewery': rating.beer.brewery.brewery_name,
		'country': rating.beer.brewery.country,
		'brewery_city': rating.beer.brewery.brewery_city,
		'beer_name': rating.beer.beer_name,
		'style': rating.beer.style,
		'plato': rating.beer.plato,
		'abv': rating.beer.abv,
		'city': rating.city,
		'place': rating.place,
		'date': rating.date,
		'price': rating.price,
		'serving': rating.serving,
		'volume': rating.volume,
		'rating': rating.rating,
		'note': rating.note,
	}
	form = BeerForm(context)
	if request.method == "POST":
		if form.is_valid():
			obj_brewery = Brewery.objects.filter(brewery_name=request.POST["brewery"]).first()
			if not obj_brewery:
				obj_brewery = Brewery()
				obj_brewery.brewery_name = request.POST["brewery"]
				obj_brewery.country = request.POST["country"]
				obj_brewery.brewery_city = request.POST["brewery_city"]
				obj_brewery.save()
			else:
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
				plato = request.POST["plato"]
				if plato:
					obj_beer.plato = plato
				else:
					obj_beer.plato = None
				abv = request.POST["abv"]
				if abv:
					obj_beer.abv = abv
				else:
					obj_beer.abv = None
				obj_beer.save()
			else:
				obj_beer.brewery = obj_brewery
				obj_beer.beer_name = request.POST["beer_name"]
				obj_beer.style = request.POST["style"]
				plato = request.POST["plato"]
				if plato:
					obj_beer.plato = plato
				else:
					obj_beer.plato = None
				abv = request.POST["abv"]
				if abv:
					obj_beer.abv = abv
				else:
					obj_beer.abv = None
				obj_beer.save()

			obj_rating = Rating.objects.filter(pk=rating_id).first()
			obj_rating.beer = obj_beer
			obj_rating.user = get_object_or_404(User, pk=request.user.id)
			obj_rating.city = request.POST["city"]
			obj_rating.place = request.POST["place"]
			posted_form = BeerForm(request.POST)
			if posted_form.is_valid():
				obj_rating.date = posted_form.cleaned_data["date"]
			obj_rating.serving = request.POST["serving"]
			price = request.POST["price"]
			if price:
				obj_rating.price = price
			else:
				obj_rating.price = None
			obj_rating.volume = request.POST["volume"]
			obj_rating.rating = request.POST["rating"]
			obj_rating.note = request.POST["note"]
			obj_rating.save()

			return HttpResponseRedirect("/beers/"+rating_id+"/")

	return render(request, "beers/editovanie_piva.html", {'form': form})

def zmazanie_hodnotenia(request, rating_id):
	Rating.objects.filter(pk=rating_id).delete()
	return HttpResponseRedirect("/beers")

def detail(request, rating_id):
	rating = Rating.objects.filter(pk=rating_id, user__id=request.user.id).select_related().first()

	return render(request, "beers/detail.html", {'rating': rating})

def pivovar_atributy(request):
	brewery_name = request.GET["brewery_name"]
	response = []
	try:
		brewery_values = Brewery.objects.filter(brewery_name=brewery_name).values().order_by("brewery_name")
		response.append(brewery_values[0])
	except Exception:
		brewery_values = None
		response.append({})

	if brewery_values:
		beers = list(Beer.objects.filter(brewery__brewery_name=brewery_name).values().order_by("beer_name"))
		response.append(beers)

	return JsonResponse(response, safe=False)

def pivo_atributy(request):
	beer_name = request.GET["beer_name"]
	try:
		beer = Beer.objects.filter(beer_name=beer_name).values().order_by("beer_name")
		return JsonResponse(beer[0], safe=False)
	except Exception:
		return JsonResponse({})