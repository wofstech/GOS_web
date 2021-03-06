from .models import Subscribe, Letter
from django import forms

class SubForm(forms.ModelForm):

    class Meta:
        model = Subscribe
        fields = ('email',)

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class Subme(forms.ModelForm):    
    class Meta:        
        model = Letter   
        fields = ('subEmail', ) 
