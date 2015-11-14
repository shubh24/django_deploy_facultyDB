from django import forms
from models import Profile,Acads,Job,Papers
from django.forms.fields import CharField


import datetime
class MyDateField(forms.DateField):

    widget = forms.DateInput(format="%d/%m/%Y")

    def __init__(self, *args, **kwargs):
        super(MyDateField, self).__init__(*args, **kwargs)
        self.input_formats = ("%d/%m/%Y",)+(self.input_formats)

    
class MyForm(forms.Form):
    
    MY_CHOICES = (
    ('1', '<='),
    ('2', '='),
    ('3', '>='),
    )
    Name = forms.ChoiceField(choices=MY_CHOICES)
    Search = forms.CharField()

class FunkyForm(forms.ModelForm):
    class Meta:
	model = Papers



class ArticleForm(forms.ModelForm):  
	class Meta:
		model = Profile
		
class AcadsForm(forms.ModelForm):  
	class Meta:
		model = Acads

class JobForm(forms.ModelForm):
     joining_date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))  
     class Meta:
	model = Job
		
