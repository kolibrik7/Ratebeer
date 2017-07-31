from django import forms
from .models import Beer
from django.utils.translation import ugettext_lazy as _
import datetime

class BeerForm(forms.ModelForm):

	date = forms.DateField(label="Dátum", widget=forms.SelectDateWidget(), initial=datetime.date.today)

	class Meta:
		model = Beer

		fields = ['brewery', 'name', 'style', 'plato', 'abv', 'city', 'place', 'date', 'serving', 
		'price', 'volume', 'note', 'rating']

		labels = {
			'brewery': _("Pivovar"),
			'name': _("Názov"),
			'style': _("Štýl"),
			'plato': _("Stupňovitosť"),
			'abv': _("Alkohol"),
			'city': _("Mesto"),
			'place': _("Podnik/Miesto"),
			'serving': _("Formát"),
			'price': _("Cena"),
			'volume': _("Objem"),
			'note': _("Poznámka"),
			'rating': _("Hodnotenie"),
		}
