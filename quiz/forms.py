from django import forms

from .forms import *

class QuizForm(forms.Form):

    choices = zip(range(3), ("A", "B", "C"))
    answer = forms.ChoiceField(label="Select your answer", choices=choices, widget=forms.RadioSelect)