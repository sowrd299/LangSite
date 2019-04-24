from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.base import TemplateView

# a hap-dash conception of "topics"
# TODO: this really belongs 1) in model and 2) in a data base
class Topic():
    def __init__(self, name, subtopics):
        self.name = name
        self.subtopics = subtopics

    # this allows us to ref the object itself in a template to get it's name
    def __str__(self):
        return self.name

topics = {
    Topic('ELD' , set()),
    Topic('Dual Language Imersion Schools' , {'Spanish', 'Croatian'}),
    Topic('The Value of Esperanto' , {'The Esperanto Thing is a Joke'}),
    Topic('English Language Standardized Tests' , {'RIP STAR Test (not really)'}),
}

topic_lookup = { t.name : t for t in topics }

# the actual view 
class ArticleView(TemplateView):

    template_name = "articles/article.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_id'] = topic_lookup[kwargs['article_id']]
        context['topics'] = topics
        return context