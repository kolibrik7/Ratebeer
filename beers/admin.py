from django.contrib import admin
from .models import Brewery, Beer, Rating

admin.site.register(Brewery)
admin.site.register(Beer)
admin.site.register(Rating)
