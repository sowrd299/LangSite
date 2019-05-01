from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('random/', views.QuizView.as_view(), name='random_question'),
]