from django.http import HttpResponse
from .models import UserData

def index(request):
    userData_list = UserData.objects.all()
    output = ', '.join([q.nom_text for q in userData_list])
    return HttpResponse(output)
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)