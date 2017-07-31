from django import forms
from .models import Beer
from django.utils.translation import ugettext_lazy as _
import datetime

class BeerForm(forms.ModelForm):

	date = forms.DateField(label="Dátum", widget=forms.SelectDateWidget(), initial=datetime.date.today)
	plato = forms.FloatField(required=False, label="Stupňovitosť", min_value=6, max_value=40,
		widget=NumberInput(attrs={'id': 'stupnovitost', 'step': "0.5"}))
	abv = forms.FloatField(required=False, label="Alkohol", min_value=0, max_value=20,
		widget=NumberInput(attrs={'id': 'alkohol', 'step': "0.1"}))
	price = forms.FloatField(required=False, label="Cena", min_value=0, max_value=5,
		widget=NumberInput(attrs={'id': 'cena', 'step': "0.1"}))


	class Meta:
		model = Beer

		fields = ['brewery', 'name', 'style', 'plato', 'abv', 'city', 'place', 'date', 'serving', 
		'price', 'volume', 'note', 'rating']

		labels = {
			'brewery': _("Pivovar"),
			'name': _("Názov"),
			'style': _("Štýl"),
			'city': _("Mesto"),
			'place': _("Podnik/Miesto"),
			'serving': _("Formát"),
			'volume': _("Objem"),
			'note': _("Poznámka"),
			'rating': _("Hodnotenie"),
		}

		widgets = {
			'serving': forms.RadioSelect
		}
