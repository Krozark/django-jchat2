# -*- coding: utf-8 -*-

from django.views.generic import TemplateView, FormView, DetailView

class HomeView(TemplateView):
    template_name = "website/home.html"
