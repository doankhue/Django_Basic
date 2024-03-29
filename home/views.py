from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader
from .models import Question
# Create your views here.

def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('home/index.html')
    context = {
        'lastest_question_list': lastest_question_list
    }
    return render(request,'home/index.html',context)
def detail(request, question_id):
    return HttpResponse("You're looking at question %s ." %question_id)
def results(request, question_id):
    response = HttpResponse("You're looking at the result of question %s .")
    return HttpResponse(response,question_id)
def vote(request, question_id):
    return HttpResponse("You're voting on question %s", question_id)