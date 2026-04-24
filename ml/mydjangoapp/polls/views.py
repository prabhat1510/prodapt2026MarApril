from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def hello(request):
    return HttpResponse("Hello, All. Welcome to django-polls")

def question(request):
    #return render(request, "ques1.html")
    return HttpResponse("Question 1: What is your name?")

def listOfQuestion(request):
    list_of_questions = ["Question 1: What is your name?", "Question 2: What is your age?", "Question 3: What is your gender?"]
    return HttpResponse("<br>".join(list_of_questions))

def getAnswer(request,question_id):
    return HttpResponse("You are looking for the answer to question "+str(question_id))
