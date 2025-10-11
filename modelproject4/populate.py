import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modelproject4.settings')
import django
django.setup()

from testapp.models import HydJobs, BanJobs, PuneJobs   
from faker import Faker
from random import *
faker = Faker()

def phonenumbergen():
    d1 = randint(6,9)
    num = ''+str(d1)
    for i in range(9):
        num += str(randint(0,9))
        return int(num)
    
def populate(n):
    for i in range(n):
        fdate = faker.date()
        fcompany = faker.company()
        ftitle = faker.random_element(elements=('project manager', 'software engineer', 'Team lead'))
        feligibility = faker.random_element(elements = ('B.tech', 'Mtech', 'BSc'))
        faddress = faker.address()
        fphonenumber = phonenumbergen()
        HydJobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle, eligibility=feligibility, address=faddress, phonenumber=fphonenumber)
        BanJobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle, eligibility=feligibility, address=faddress, phonenumber=fphonenumber)
        PuneJobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle, eligibility=feligibility, address=faddress, phonenumber=fphonenumber)

n = int(input('enter no. of records:'))
populate(n)
print(f'{n} record inserts')
