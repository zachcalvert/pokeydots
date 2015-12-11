from django.db import models


class Neighborhood(models.Model):
	name = models.CharField(max_length=50)


class Spot(models.Model):
	name = models.CharField(max_length=50)
	neighborhood = models.ForeignKey(Neighborhood)
	address = models.CharField(max_length=75, null=True, blank=True)

	class Meta:
		abstract = True
		ordering = ['name']

	def get_subclass(self):
		if type(self) != Spot:
			return self
		return Spot.objects.get_subclass(id=self.id)


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
	late_night = models.BooleanField(default=False)


class Bar(Spot):
	has_games = models.BooleanField(default=False)
	has_sports = models.BooleanField(default=False)
	is_dive = models.BooleanField(default=False)


class Home(Spot):
	capacity = models.IntegerField(default=1)





