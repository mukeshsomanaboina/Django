from django.contrib import admin
from testapp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('rollno', 'name', 'marks', 'email', 'phonenumber', 'address')

admin.site.register(Student, StudentAdmin)

