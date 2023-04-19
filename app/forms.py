from django import forms
g=[('FEMALE','female'),('MALE','male')]
d=[['PYTHON','python'],('SQL','sql'),('HTML','html')]
class studentForm(forms.Form):

    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    date=forms.DateField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    address=forms.CharField(max_length=100,widget=forms.Textarea(attrs={'cols':5,'rows':3}))
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #course=forms.MultipleChoiceField(choices=d)
    course=forms.MultipleChoiceField(choices=d,widget=forms.CheckboxSelectMultiple)


