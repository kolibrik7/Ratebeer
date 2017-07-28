from django.db import models

class Beer(models.Model):
	STYLE_CHOICES = (
		("lager", "Ležiak"),
		("ale", "Ale"),
	)

	brewery = models.CharField(max_length=50)
	name = models.CharField(max_length=70)
	style = models.CharField(
		max_length=20,
		choices="STYLE_CHOICES"
	)
	plato = models.IntegerField()
	abv = models.FloatField()
	city = models.CharField(max_length=50)
	place = models.CharField(max_length=70)
	note = models.TextField()