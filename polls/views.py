"""Manejo de los views del sitio web"""
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from .models import Question, Choice
# Create your views here.

def index(request):
    """Crea la view principal, una lista de las ultimas 5 preguntas"""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
def detail(request, question_id):
    """Devuelve la view para preguntas especificas"""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})
def results(request, question_id):
    """Devuelve el resultado para una pregunta especifica"""
    return HttpResponse("Estas viendo el resultado de {}".format(question_id))
def vote(request, question_id):
    """Devuelve la view para votar una pregunta"""
    question = get_object_or_404(Question, question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST('choice'))
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
