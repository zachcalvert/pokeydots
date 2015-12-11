from django.db import models
from django.contrib.auth.models import User

from locations.models import Spot, Home


class SpotToUser(models.Model):
	spot = models.ForeignKey(Spot, related_name='spot_to_users')
	user = models.ForeignKey('UserProfile', related_name='spot_to_users')
	home = models.ForeignKey(Home)

	class Meta:
		ordering = ['spot']
		unique_together = (
			['spot', 'user'],
		)


class UserProfile(models.Model):
	"""
	A user profile model for tracking additional user metadata.
	"""
	user = models.OneToOneField(User, related_name='profile')
	favorite_spots = models.ManyToManyField(
		Spot,
		through=SpotToUser,
		related_name='users'
	)

	# Used to track how this user profile object was created
	source = models.CharField(max_length=10, default="admin")

	favorite_spots

	def __unicode__(self):
		return u'%s <%s>' % (self.user.get_full_name(), self.user.email,)

	def get_absolute_url(self):
		return reverse('user_profile', kwargs={'user_id': self.user.pk})