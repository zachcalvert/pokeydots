from django.db import models

# Create your models here.


class Neighborhood(models.Model):
	name = models.CharField(max_length=50)


class Spot(models.Model):
	name = models.CharField(max_length=50)
	neighborhood = models.ForeignKey(Neighborhood)
	address = models.CharField(max_length=75, null=True, blank=True)

	class Meta:
		abstract = True


RESTAURANT_TYPES = (
	('mexican', 'Mexican'),
	('sushi', 'Sushi'),
	('thai', 'Thai'),
	('american', 'American'),
)

class Restaurant(Spot):
	genre = models.CharField(max_length=30, choices=RESTAURANT_TYPES, 
		help_text='What kind of restaurant is this?')
	has_liquor = models.BooleanField(default=False)


BAR_TYPES = (
	('swanky', 'Swanky'),
	('divey', 'Dive'),
)

class Bar(Spot):
	genre = models.CharField(max_length=30, choices=BAR_TYPES, 
		help_text='What kind of bar is this?')
	has_games = models.BooleanField(default=False)


