from django import forms
from .models import Registor

class RegistorForm(forms.ModelForm):
    class Meta:
        model = Registor
        fields = "__all__" 
class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')