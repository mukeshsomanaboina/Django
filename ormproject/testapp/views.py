from django.shortcuts import render
from testapp.models import Employee

def retrieve_view(request):
    # emp_list = Employee.objects.all()
    # emp_list = Employee.objects.filter(esal__gte=25000)
    # emp_list = Employee.objects.filter(esal__lte =25000)
    # emp_list = Employee.objects.filter(ename__startswith = 'm')
    # emp_list = Employee.objects.filter(ename__endswith = 'h')
    emp_list = Employee.objects.filter(esal__range=[15000,26000])

    return render(request, 'testapp/index.html', {'emp_list': emp_list})