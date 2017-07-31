from django.db import models

class Beer(models.Model):

	

	brewery = models.CharField(max_length=50)
	name = models.CharField(max_length=70)
	style = models.CharField(
		max_length=10,
		#choices='STYLE_CHOICES',
		#default='ale'
	)
	plato = models.IntegerField()
	abv = models.FloatField()
	city = models.CharField(max_length=50)
	place = models.CharField(max_length=70)
	serving = models.BooleanField() # sud alebo flasa
	date = models.DateField()
	price = models.FloatField()
	volume = models.CharField(max_length=10) # choices
	note = models.TextField()