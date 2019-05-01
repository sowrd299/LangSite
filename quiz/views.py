from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import QuizForm
from .models import Question

# Create your views here.

# view a quiz question
def quiz(request):

    question = Question.objects.get(prompt="How much wood would a wood check chuck if a wood chuck could chuck wood?")

    if request.method == 'POST':
        pass
    
    form = QuizForm(question)

    return render(request, "quiz/quiz.html", {'form' : form, 'question' : question})