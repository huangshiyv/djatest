from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import Http404
from .models import UserData
from django.urls import reverse
import datetime


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import requests 


from django.views.decorators.csrf import csrf_exempt

def index(request):
    userData_list = UserData.objects.all()
    context = {
        'userData_list': userData_list,
        "nav_active": "dashboard"
    }
    return render(request, 'polls/index.html', context)


def detail(request, id):
    userData = get_object_or_404(UserData, pk=id)
    return render(request, 'polls/detail.html', {'userdata': userData})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, id):
    return HttpResponse("You're voting on question %s." % id)


@csrf_exempt
def getRecap(request, id):
    recapToken = request.POST['choice']
    recapData = UserData(tele_text="12345", startprocess_date=datetime.datetime.now(
    ), endprocess_date=datetime.datetime.now(), state_int=0)
    recapData.save()
    return HttpResponseRedirect(reverse('polls:results', args=(recapData.id,)))


def upload_csv1(request):
    data = {}
    if "GET" == request.method:
        return render(request, "polls/upload_csv.html", data)
    # if not GET, then proceed
    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            return HttpResponseRedirect(reverse("polls:upload_csv"))
    # if file is too large, return
        if csv_file.multiple_chunks():
            return HttpResponseRedirect(reverse("polls:upload_csv"))

        file_data = csv_file.read().decode("utf-8")

        lines = file_data.split("\n")
        # loop over the lines and save them in db. If error , store as string and then display
        for line in lines[1:]:
            fields = line.split(",")
            if len(fields) != 6:
                continue
            data_dict = {}
            data_dict["nom_text"] = fields[0]
            data_dict["prenom_text"] = fields[1]
            data_dict["tele_text"] = fields[2]
            data_dict["email_text"] = fields[3]
            data_dict["passeport_text"] = fields[4]
            data_dict["startprocess_date"] = datetime.datetime.now()
            data_dict["endprocess_date"] = datetime.datetime.now()
            data_dict["state_int"] = 0
            data_dict["notifytele_text"] = "0699342394"
            try:
                m = UserData(**data_dict)
                m.save()
            except Exception as e:
                pass

    except Exception as e:
        pass

    return HttpResponseRedirect(reverse("polls:upload_csv"))
def upload_csv(request):

    mobile_emulation = { "deviceName": "iPhone X" }
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Chrome(executable_path = 'chromedriver',chrome_options=chrome_options)
    driver.get('https://www.hermesfaubourg.com/client/register?lang=fr')

    #driver.get('https://dashboard.nexmo.com/sign-up')

    search_box_surname = driver.find_element_by_name('surname')
    search_box_surname.send_keys('Devin Mancuso')
    search_box_name = driver.find_element_by_name('name')
    search_box_name.send_keys('Ddddd')

    search_box_phonesuffix = Select(driver.find_element_by_id("phone_country"))
    search_box_phonesuffix.select_by_value('FR')

    search_box_phone = driver.find_element_by_name('phone_number')
    search_box_phone.send_keys('0699342394')

    search_box_email = driver.find_element_by_name('email')
    search_box_email.send_keys('huangshiyv@gmail.com')

    search_box_pass = driver.find_element_by_name('passport_id')
    search_box_pass.send_keys('passsss')


    search_box_CGU = driver.find_element_by_name('cgu')
    search_box_CGU.click()