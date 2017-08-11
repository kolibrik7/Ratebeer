from django.db import models
import django.utils.timezone

class Beer(models.Model):

	brewery = models.CharField(max_length=50)

	COUNTRY_CHOICES = (
		('SK', 'Slovensko'),
		('CZ', 'Česká republika'),
		('US', 'USA'),
	)
	country = models.CharField(max_length=30, choices=COUNTRY_CHOICES, default='SK')
	name = models.CharField(max_length=70)

	STYLE_CHOICES = (
			('altbier', 'Altbier'),
			('amber', 'Amber Ale'),
			('apa', 'APA'),
			('american_strong', 'American Strong Ale'),
			('baltic', 'Baltic Porter'),
			('barley_wine', 'Barley Wine'),
			('belgian', 'Belgian Ale'),
			('belgian_strong', 'Belgian Strong Ale'),
			('berliner_weisse', 'Berliner Weisse'),
			('biere_de_garde', 'Biere de Garde'),
			('bitter', 'Bitter'),
			('black_ipa', 'Black IPA'),
			('brown', 'Brown Ale'),
			('spice_herb_vegetable', 'Byliny/Korenie/Zelenina'),
			('california_common', 'California Common'),
			('cider', 'Cider'),
			('cream', 'Cream Ale'),
			('doppelbock', 'Doppelbock'),
			('dry_stout', 'Dry Stout'),
			('dubbel', 'Dubbel'),
			('dunkelweizen', 'Dunkelweizen'),
			('dunklerbock', 'Dunkler Bock'),
			('eisbock', 'Eisbock'),
			('epa', 'EPA'),
			('english_strong', 'English Strong Ale'),
			('foreign_stout', 'Foreign Stout'),
			('gose', 'Gose/Grodziskie'),
			('golden', 'Golden Ale/Blond Ale'),
			('hefeweizen', 'Hefeweizen'),
			('hellerbock', 'Heller Bock'),
			('helles', 'Helles'),
			('imperial_ipa', 'Imperial IPA/Double IPA'),
			('imperial_pils', 'Imperial Pils/Strong Lager'),
			('imperial_porter', 'Imperial Porter'),
			('imperial_stout', 'Imperial Stout'),
			('ipa', 'IPA'),
			('ipl', 'IPL'),
			('irish', 'Irish Ale'),
			('kolsch', 'Kölsch'),
			('kristallweizen', 'Kristallweizen'),
			('lambic', 'Lambic'),
			('marzen', 'Märzen/Oktoberfest'),
			('mild', 'Mild Ale'),
			('nealko', 'Nealkoholické'),
			('old', 'Old Ale'),
			('fruit', 'Ovocné'),
			('polotmavy', 'Polotmavý ležiak'),
			('porter', 'Porter'),
			('esb', 'Premium Bitter/ESB'),
			('quadrupel', 'Quadrupel'),
			('radler', 'Radler'),
			('sahti', 'Sahti'),
			('saison', 'Saison'),
			('scotch', 'Scotch Ale'),
			('scottish', 'Scottish Ale'),
			('session_ipa', 'Session IPA'),
			('sour', 'Sour Ale'),
			('stout', 'Stout'),
			('svetly', 'Svetlý ležiak'),
			('sweet_stout', 'Sweet Stout/Milk Stout'),
			('tmavy', 'Tmavý ležiak'),
			('traditional', 'Traditional Ale'),
			('tripel', 'Tripel'),
			('smoked', 'Údené'),
			('vienna', 'Viedenský ležiak'),
			('weizenbock', 'Weizen Bock'),
			('wheat', 'Wheat Ale'),
			('witbier', 'Witbier'),
			('zwickel', 'Zwickel/Keller'),
	)
	style = models.CharField(
		max_length=10,
		choices=STYLE_CHOICES,
		default='lager'
	)

	plato = models.FloatField(null=True, blank=True)
	abv = models.FloatField(null=True, blank=True)
	city = models.CharField(max_length=50)
	place = models.CharField(max_length=70)

	SERVING_CHOICES = (
		(True, 'Fľaša'),
		(False, 'Sud'),
	)
	serving = models.BooleanField(choices=SERVING_CHOICES, default=True) # sud alebo flasa

	date = models.DateField(default=django.utils.timezone.now)
	price = models.FloatField(null=True, blank=True)

	DECI = 0.1
	DVE_DECI = 0.2
	MALE = 0.33
	STVORKA = 0.4
	VELKE = 0.5
	SEDMICKA = 0.75
	LITER = 1
	VOLUME_CHOICES = (
		(DECI, '0,1l'),
		(DVE_DECI, '0,2l'),
		(MALE, '0,33l'),
		(STVORKA, '0.4l'),
		(VELKE, '0,5l'),
		(SEDMICKA, '0,75l'),
		(LITER, '1l'),
	)
	volume = models.FloatField(max_length=10, choices=VOLUME_CHOICES, default=VELKE) # choices

	note = models.TextField()

	ZLE = 1
	PODPRIEMER = 2
	PRIEMER = 3
	NADPRIEMER = 4
	SUPER = 5
	RATING_CHOICES = (
		(ZLE, '1'),
		(PODPRIEMER, '2'),
		(PRIEMER, '3'),
		(NADPRIEMER, '4'),
		(SUPER, '5'),
	)
	rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=PRIEMER) #choices