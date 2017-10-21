from django import forms
from .models import Brewery, Beer, Rating
from django.utils.translation import ugettext_lazy as _
import datetime

class CustomModelChoiceField(forms.ModelChoiceField):
	def to_python(self, value):
		if value in self.empty_values:
			return None
		"""
		key = self.to_field_name or 'pk'
		try:
			value2 = self.queryset.get(**{key: value})
			return value2
		except Exception:
		"""
		return value

class BeerForm(forms.Form):

	def years():
		current_year = datetime.datetime.now().year
		first_year = current_year - 5
		return list(range(first_year, current_year + 1))

	brewery = CustomModelChoiceField(label="Pivovar", queryset=Brewery.objects.all().order_by("brewery_name"), to_field_name="brewery_name")
	country = forms.CharField(label="Krajina", widget=forms.Select(choices=Brewery.COUNTRY_CHOICES), initial='SK')
	brewery_city = forms.CharField(required=False, label="Mesto")

	beer_name = CustomModelChoiceField(label="Názov", queryset=Beer.objects.all().order_by("beer_name"), to_field_name="beer_name")
	style = forms.CharField(label="Štýl", widget=forms.Select(choices=Beer.STYLE_CHOICES), initial='ipa')
	plato = forms.FloatField(required=False, label="Stupňovitosť", min_value=6, max_value=40, initial=12,
		widget=forms.NumberInput(attrs={'id': 'stupnovitost', 'step': "0.5"}))
	abv = forms.FloatField(required=False, label="Alkohol", min_value=0, max_value=20, initial=5,
		widget=forms.NumberInput(attrs={'id': 'alkohol', 'step': "0.1"}))

	city = CustomModelChoiceField(label="Mesto", queryset=Rating.objects.values_list("city", flat=True).distinct().order_by("city"))
	place = forms.CharField(required=False, label="Podnik/Miesto")
	place = CustomModelChoiceField(required=False, label="Podnik/Miesto", queryset=Rating.objects.values_list("place", flat=True).distinct().order_by("place"))
	date = forms.DateField(label="Dátum", widget=forms.SelectDateWidget(years=years()), initial=datetime.date.today)
	price = forms.FloatField(required=False, label="Cena", min_value=0, max_value=10, initial=1.5,
		widget=forms.NumberInput(attrs={'id': 'cena', 'step': "0.01"}))
	serving = forms.BooleanField(required=False, label="Formát", widget=forms.RadioSelect(choices=Rating.SERVING_CHOICES), initial=True)
	volume = forms.FloatField(label="Objem", widget=forms.Select(choices=Rating.VOLUME_CHOICES), initial=Rating.VELKE)
	rating = forms.IntegerField(label="Hodnotenie", widget=forms.Select(choices=Rating.RATING_CHOICES), initial=3)
	note = forms.CharField(required=False, label="Poznámka", widget=forms.Textarea())
