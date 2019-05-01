from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('<str:article_id>/read/', views.ArticleView.as_view(), name='article'),
    path('quiz/', views.QuizView.as_view(), name='quiz'),
]