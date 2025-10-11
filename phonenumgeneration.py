from random import *
from faker import Faker
def phonenumbergen():
    x = randint(6,9)
    s = str(x)
    for i in range(0,9):
        y = str(randint(0,9))
        s += y
    return s    

def fake(n):
    f = Faker()
    for i in range(n):
        frollno = f.random_int(min=1, max=999)
        fname = f.name()
        fphone=phonenumbergen()
        faddress=f.address()
        fdob=f.date()
        fmarks=f.random_int(min=1, max=100) 
        femail=f.email()
        print()
        print (frollno,fname,fphone,faddress,fdob,fmarks,femail)
        print()
n=int(input("Enter the number of fake data you want: "))
fake(n)