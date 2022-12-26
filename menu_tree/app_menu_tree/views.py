from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """
    Отображение главной страницы (index)
    """

    template_name = 'index.html'
