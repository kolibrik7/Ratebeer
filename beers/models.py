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
			('ale', 'Ale'),
			('lager', 'Ležiak'),
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
	VELKE = 0.5
	SEDMICKA = 0.75
	LITER = 1
	VOLUME_CHOICES = (
		(DECI, '0,1l'),
		(DVE_DECI, '0,2l'),
		(MALE, '0,33l'),
		(VELKE, '0,5l'),
		(SEDMICKA, '0,75l'),
		(LITER, '1l'),
	)
	volume = models.CharField(max_length=10, choices=VOLUME_CHOICES, default=VELKE) # choices

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