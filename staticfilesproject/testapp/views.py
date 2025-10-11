
from django.shortcuts import render

def static_view(request):
    subjects = {'s1':'python', 's2':'Django', 's3':'Rest APIs', 's4':'Numpy'}
    return render(request, 'testapp/results.html', subjects)