from django import template
from polls.models import Question
from django.shortcuts import render
from django.http import HttpResponse, response
from django.template import loader
from django.http import HttpResponse, response, Http404

def index(request):
    all_questions = Question.objects.order_by("-publication_date")
    template = loader.get_template("polls/index.html")
    context = {"all_questions": all_questions}
    return render(request, "polls/index.html", context)

def results(request, question_id):
    response = f"Список ответов на ваши вопросы {question_id} results" 
    return HttpResponse(response)

def vote(request, question_id):
    response = f"Ваш ответ на {question_id}"
    return HttpResponse(response)

def detail(request, question_id):
    response = f"Вы чиитаете вопрос {question_id}"
    return HttpResponse(response)