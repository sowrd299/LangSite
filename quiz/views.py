from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import QuizForm

# Create your views here.

class QuizView(FormView):

    template_name = 'quiz/quiz.html'
    form_class = QuizForm
    success_url = '/quiz/random/' # TODO: use the URL lib. to handle this

    # TODO: does this actually get called in FormView?
    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    '''

    def form_valid(self, form):
        return super().form_valid(form)
