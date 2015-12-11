from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class UserProfileView(TemplateView):
	template_name = 'user_profile.html'

	def get_context_data(self, **kwargs):
		context = super(UserProfileView, self).get_context_data(**kwargs)
		if self.request.user.is_authenticated():
			user = get_object_or_404(User, pk=self.request.user.pk)
		else:
			return reverse('login')

		context['user'] = user
		return context