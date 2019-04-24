from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

topics = {
    'ELD',
    'Dual Language Imersion Schools',
    'The Value of Esperanto',
    'The Esperanto Thing is a Joke',
    'English Language Standardized Tests',
}

def article(request, article_id):
    #return HttpResponse('<h1>Hello! %s</h1>' % article_id)
    context = {
        'article_id' : article_id,
        'topics' : topics,
    }
    return render(request, 'articles/article.html', context)