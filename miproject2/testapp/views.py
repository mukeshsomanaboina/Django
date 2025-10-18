from django.shortcuts import render

from testapp.models import Employee

def display_view(request):
    # emp_list = Employee.objects.all()
    # emp_list = Employee.objects.get_emp_sal_range(60000, 700000)
    emp_list = Employee.objects.get_emp_sorted_by('ename')
    return render(request, 'testapp/index.html', {'emp_list':emp_list})