from django import forms

class QuizForm(forms.Form):

    answer = forms.ChoiceField(("A", "B", "C"))