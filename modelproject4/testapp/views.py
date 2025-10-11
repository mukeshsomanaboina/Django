from django.shortcuts import render
from testapp.models import HydJobs, BanJobs, PuneJobs

def home_page(request):
    return render(request, 'testapp/index.html')


def hyd_jobs_view(request):
    jobs_list = HydJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request, 'testapp/hydjobs.html', my_dict)

def ban_jobs_view(request):
    jobs_list = BanJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request, 'testapp/hydjobs.html', my_dict)


def pune_jobs_view(request):
    jobs_list = PuneJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request, 'testapp/hydjobs.html', my_dict)