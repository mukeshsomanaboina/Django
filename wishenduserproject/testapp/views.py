from django.shortcuts import render
import datetime

def wish(request):
    date = datetime.datetime.now()
    msg = 'Hello Guest very'
    h = int(date.strftime('%H'))
    if h <= 12:
        msg = 'Gd Mrng'
    elif h<=16:
        msg = 'Gd Afternoon'
    elif h<=21:
        msg = 'Gd Evng'
    else:
        msg = 'Gd Nt'
    my_dict = {'insert_date':date, 'insert_msg':msg}
    return render(request,'testapp/wish.html',context=my_dict)