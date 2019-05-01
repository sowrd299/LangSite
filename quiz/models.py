from django.db import models

# a question in the quiz
class Question(models.Model):
    prompt = models.TextField(default = "ERROR: QUESTION MISSING")

    def __str__(self):
        return self.prompt

# the answer to a question in the quiz
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    value = models.TextField(default = "ERROR: ANSWER TEXT MISSING")
    correct = models.BooleanField()

    def __str__(self):
        return self.value
