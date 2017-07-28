from django.shortcuts import render

from .models import Beer

def zoznam(request):
	return render(request, "beers/zoznam.html")
