from django.urls import path

from . import views

urlpatterns = [
    #localhost:8000/polls/hello
    path("hello", views.hello, name="hello"),
    #localhost:8000/polls/question
    path("question", views.question, name="question"),
    #localhost:8000/polls/  
    path("", views.index, name="index"),
]