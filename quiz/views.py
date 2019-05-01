from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import QuizForm
from .models import Question
from .models import Answer
from articles.models import Topic

# Create your views here.

# view a quiz question
def quiz(request):
    
    context = dict()

    question = Question.objects.get(prompt="How much wood would a wood check chuck if a wood chuck could chuck wood?")

    if request.method == 'POST':
        # handle answer questions
        context['prev_answer'] = Answer.objects.get(id = request.POST.get('answer'))
    
    context['form'] = QuizForm(question)
    context['question'] = question
    context['topics'] = Topic.objects.all() # TODO: this feels like tentacles; and also redundent code

    return render(request, "quiz/quiz.html", context=context)