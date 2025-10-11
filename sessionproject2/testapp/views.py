from django.shortcuts import render
from testapp.forms import LoginForm

def home_view(request):
    forms = LoginForm()
    return render(request, 'testapp/home.html',{'forms':forms})

def date_time(request):
    name = request.GET['name']
    response = render(request, 'testapp/datetime.html', {'name':name})
    response.set_cookie('name', name)
    return response 

import datetime
def results_view(request):
    name = request.COOKIES.get('name')
    date_time = datetime.datetime.now()
    return render(request,'testapp/results.html', {'name':name, 'date_time':date_time})
