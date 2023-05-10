from django import forms

def check_for_a(Val):
    if Val[0].lower()=='a':
        raise forms.ValidationError('name should not start with a ')
def check_len(Value):
    if len(Value)<5:
        raise forms.ValidationError('Lenght shoulb be more than five..')

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a,check_len])
    age=forms.IntegerField()
    email=forms.EmailField()
    re_enter_email=forms.EmailField()
    

    
    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['re_enter_email']

        if e!=r:
            raise forms.ValidationError('Incorrect email....')
