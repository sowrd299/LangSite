from django import forms

class QuizForm(forms.Form):

    def __init__(self, question, *args, **kwargs):
        #question = kwargs.pop('question')
        super().__init__(*args, **kwargs)

        # get the answers to the given question
        answers = question.answer_set.all()
        # format the answers for the form
        # choices = zip(range(len(answers)), answers)
        choices = tuple( (x.id, x) for x in answers )

        self.fields['answer'] = forms.ChoiceField(label="Select your answer", choices=choices, widget=forms.RadioSelect)