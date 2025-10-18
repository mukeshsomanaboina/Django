import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miproject2.settings')

import django
django.setup()

from testapp.models import Employee
from faker import Faker
from random import *
faker = Faker()

def populate(n):
    for i in range(n):
        feno = randint(1,100)
        fename = faker.name()
        fesal = randint(40000,100000)
        feaddr = faker.city()
        emp_records = Employee.objects.get_or_create(
            eno = feno, ename = fename, esal = fesal, eaddr = feaddr
        )
n = int(input('enter number of employees:'))
populate(n)
print(f'{n} inserted successfully')