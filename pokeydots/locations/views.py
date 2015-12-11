import json

from django.http import Http404, HttpResponse
from django.template.response import TemplateResponse
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.views.generic import View, TemplateView

from models import Spot, Restaurant, Bar


class HomeView(TemplateView):