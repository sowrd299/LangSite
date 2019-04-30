from django.contrib import admin

from .models import Topic
from .models import Subtopic

admin.site.register(Topic)
admin.site.register(Subtopic)

# Register your models here.
