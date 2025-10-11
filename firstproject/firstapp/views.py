from django.shortcuts import render
import datetime
from django.http import HttpResponse

def date_time_info(request):
    date=datetime.datetime.now()
    h = int(date.strftime('%H'))
    msg = '<h1> Hello Guest Very '
    if h < 12:
        msg += 'Gd Mrng'
    elif h < 16:
        msg += 'Gd Aftrnoon'
    elif h < 21:
        msg += 'Gd Evng'
    else:
        msg += 'Gd Nt'
    msg += '</h1><hr>'
    msg += '<h2> Time:'+str(date)+'</h2>'
    return HttpResponse(msg)
