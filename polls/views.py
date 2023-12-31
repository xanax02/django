from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse , Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
# from django.template import loader

from .models import Question, Choice

# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     # template = loader.get_template("polls/index.html")
#     context = {"latest_question_list": latest_question_list}
#     # return HttpResponse(template.render(context, request))
#     return render(request, "polls/index.html", context)


# def detail(request, question_id):
#     # try:
#         # question = Question.objects.get(id=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question Does not exist")
#     question = get_object_or_404(Question, id = question_id)
#     return render(request, 'polls/details.html', {"question": question})


# def results(request, question_id):
#     question = get_object_or_404(Question, id = question_id)
#     return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, id = question_id)
    try:
        selected_choice = question.choice_set.get(id = request.POST["choice"])
    except:
        return render(request, 'polls/details.html', {"question": question, "error_message": "Your havenot selected any choice"})
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    

# # Generic views
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]
    

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/details.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/resuls.html"