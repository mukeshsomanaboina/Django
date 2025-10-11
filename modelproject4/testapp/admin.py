from django.contrib import admin
from testapp.models import HydJobs, BanJobs, PuneJobs

class HydJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'phonenumber']
admin.site.register(HydJobs, HydJobsAdmin)


class BanJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'phonenumber']
admin.site.register(BanJobs, BanJobsAdmin)


class PuneJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'phonenumber']
admin.site.register(PuneJobs, PuneJobsAdmin)