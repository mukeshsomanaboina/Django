from django.shortcuts import render

def home_page_view(request):
    return render(request,'testapp/home.html')

# def java_page_view(request):
#     return render(request,'testapp/javaexams.html')

def python_page_view(request):
    return render(request,'testapp/pythonexams.html')

def aptitude_page_view(request):
    return render(request,'testapp/aptitude.html')

from django.contrib.auth.decorators import login_required
@login_required
def java_page_view(request):
    return render(request,'testapp/javaexams.html')