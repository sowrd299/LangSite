from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import QuizForm
from .models import Question
from .models import Answer
from articles.models import Topic

from random import randint
from django.db.models.aggregates import Count

# Create your views here.

# view a quiz question
def quiz(request):
    
    context = dict()

    # rand int
    # code thanks to https://stackoverflow.com/questions/962619/how-to-pull-a-random-record-using-djangos-orm
    count = Question.objects.aggregate(count=Count('id'))['count']
    random_index = randint(0, count - 1)
    question = Question.objects.all()[random_index]

    if request.method == 'POST':
        # handle answer questions
        context['prev_answer'] = Answer.objects.get(id = request.POST.get('answer'))
    
    context['form'] = QuizForm(question)
    context['question'] = question
    context['topics'] = Topic.objects.all() # TODO: this feels like tentacles; and also redundent code

    return render(request, "quiz/quiz.html", context=context)