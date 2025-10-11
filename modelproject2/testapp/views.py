from django.shortcuts import render
from testapp.models import Employee

def emp_data_view(request):
    emp_list = Employee.objects.all()
    return render(request, 'testapp/emp.html',{'my_dict':emp_list})
