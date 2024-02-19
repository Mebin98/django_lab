from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render

# Create your views here.

def index(request):
    """
    # return HttpResponse("Hello, World!\n")
    # 출판 날짜별로 데이터를 상위 5개 정렬된거 나오고
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 그 데이터들을 ',' 로 연결함
    output = ', '.join([q.question_text for q in lastest_question_list])
    return HttpResponse(output)
    """
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : lastest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})



    return HttpResponse("You`re looking at question %s." % question_id)

def results(request, question_id):
    response = "You`re looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You`re voting on question %s." & question_id)

