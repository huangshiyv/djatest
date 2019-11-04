from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.template import loader
from django.http import Http404
from .models import UserData
from django.urls import reverse
def index(request):
    userData_list = UserData.objects.all()
    context = {
        'userData_list': userData_list,
    }
    return render(request, 'polls/index.html', context)
def detail(request, id):
    userData = get_object_or_404(UserData,pk=id)
    return render(request, 'polls/detail.html', {'userdata': userData})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def getRecap(request, id):
    recapToken = request.POST['choice']
    recapData = UserData(tele_text="12345")
    recapData.save()
    return HttpResponseRedirect(reverse('polls:results', args=(recapData.id,)))