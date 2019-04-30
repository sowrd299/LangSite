from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.base import TemplateView
from django.core import exceptions

from .models import *

# the actual view 
class ArticleView(TemplateView):

    template_name = "articles/article.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['article_id'] = Topic.objects.get(name=kwargs['article_id'])
        except exceptions.ObjectDoesNotExist:
            # non-existant articles can be handled gracefully by the template
            context['article_id'] = None
        context['topics'] = Topic.objects.all()
        return context

class QuizView(TemplateView):

    pass