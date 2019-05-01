from django.db import models

# Create your models here.

# a hap-dash conception of "topics"
class Topic(models.Model):
    name = models.CharField(max_length=64)
    index = models.IntegerField(default=-1)

    # this allows us to ref the object itself in a template to get it's name
    def __str__(self):
        return self.name

    # this is just here so I didn't have to refactor the template
    def subtopics(self):
        return self.subtopic_set.all()

class Subtopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    text = models.TextField(default = "<p>ERROR: TEXT MISSING</p>")
    index = models.IntegerField(default = -1)

    # this allows us to ref the object itself in a template to get it's name
    def __str__(self):
        return self.name
