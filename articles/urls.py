from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('<str:article_id>/read/', views.article, name='article')
]