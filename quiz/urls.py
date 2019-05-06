from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('random/', views.quiz, name='random_question'),
]