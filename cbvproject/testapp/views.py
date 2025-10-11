from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class HelloWorld(View):
    def get(self, request):
        return HttpResponse('<h1> response from class based view </h1>')

from django.views.generic import TemplateView
class TemplateCbv(TemplateView):
    template_name = 'testapp/results.html'


class TemplateCbv2(TemplateView):
    template_name = 'testapp/results2.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'sunny'
        context['marks'] = 98
        context['subject'] = 'python'
        return context
