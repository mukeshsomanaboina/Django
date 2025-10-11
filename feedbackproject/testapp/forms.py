from django import forms

class FeedBackForm(forms.Form):
    name = forms.CharField(max_length=200)
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        print('validating name field')
        input_name = self.cleaned_data['name']
        if len(input_name)<3:
            raise forms.ValidationError('Name must be at least 3 characters long')
        return input_name
    def clean_rollno(self):
        print('validating roll no')
        input_rollno = self.cleaned_data['rollno']
        if int(input_rollno)<1:
            raise forms.ValidationError(' should be more than 0')
        return input_rollno
    def clean_email(self):
        print('validating email')
        input_email=self.cleaned_data['email']
        return input_email
    def clean_feedback(self):
        print('validating email')
        input_feedback = self.cleaned_data['feedback']
        return input_feedback
    
    

