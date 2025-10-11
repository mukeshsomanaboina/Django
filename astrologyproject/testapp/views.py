from django.shortcuts import render
import datetime, random

def result_view(request):
    msg_list = [
        'Golden days ahead',
        'Soon getting Job',
        'proposing gf tmrw',
        'No love'
    ]
    names_list=[
        'sunny','Kareena', 'Katrina', 'priya', 'Baby'
    ]
    time = datetime.datetime.now()
    h = int(time.strftime('%H'))
    if h<12:
        s = 'Gd Mrng'
    elif h<16:
        s = 'Gd Aftrnoon'
    elif h<21:
        s = 'Gd Evng'
    else:
        s = 'Gd Nt'
    name = random.choice(names_list)
    msg = random.choice(msg_list)
    my_dict = {'time':time, 'name':name, 'msg':msg, 'wish':s}
    return render(request, 'testapp/astrology.html',my_dict)