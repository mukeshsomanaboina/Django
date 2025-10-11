from django.shortcuts import render
from testapp.forms import FeedBackForm


def feedback_view(request):
    submitted = False
    name = ''
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            print('Form Validation success')
            print('*'*100)
            print('Name:', form.cleaned_data['name'])
            print('RollNo:',form.cleaned_data['rollno'])
            print('Email:', form.cleaned_data['email'])
            print('Feedback:', form.cleaned_data['feedback'])
            submitted = True
            name = form.cleaned_data['name']
    form = FeedBackForm()
    return render(request, 'testapp/feedback.html', {'form':form, 'submitted':submitted, 'name':name})

