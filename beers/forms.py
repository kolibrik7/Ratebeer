from django import forms
from .models import Beer
from django.utils.translation import ugettext_lazy as _

class BeerForm(forms.ModelForm):



	class Meta:
		model = Beer
		fields = ['brewery', 'name', 'style', 'plato', 'abv', 'city', 'place', 'date', 'serving', 
		'price', 'volume', 'note', 'rating']
		labels = {
			'brewery': _("Pivovar"),
			'name': _("Názov"),
			'style': _("Štýl"),
			'plato': _("Stupňovitosť"),
			
		}