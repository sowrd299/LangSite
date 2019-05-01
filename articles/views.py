from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.core import exceptions

from .models import *
from .forms import *

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

#TODO: the degree that quiz should be it's own app is large
class QuizView(FormView):

    template_name = 'articles/article.html'
    form_class = QuizForm
    success_url = '/articles/quiz/' # TODO: use the URL lib. to handle this

    # TODO: does this actually get called in FormView?
    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    '''

    def form_valid(self, form):
        return super().form_valid(form)