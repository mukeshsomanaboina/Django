from django.shortcuts import render
from django.http import HttpResponse

def hydjobsinfo(request):
    s = '<h1> Hyd jobs info </h1>'
    return HttpResponse(s)
def bngjobsinfo(request):
    s='<h1> Bng jobs info </h1>'
    return HttpResponse(s)
def punejobsinfo(request):
    s='<h1> pune jobs info <h1>'
    return HttpResponse(s)