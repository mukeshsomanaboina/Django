from django.shortcuts import render
from django.http import HttpResponse

def welcome_view(request):
    print('this line added by view function')
    return HttpResponse('<h1> custom middleware demo</h1>')
