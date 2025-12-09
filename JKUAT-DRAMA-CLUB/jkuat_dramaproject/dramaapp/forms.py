from django.forms import ModelForm
from  .models import member, event, gallery
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class memberForm(ModelForm):
    class Meta:
        model = member
        fields = '__all__' 
        
class eventForm(ModelForm):
    class Meta:
        model = event
        fields = '__all__' 

class galleryForm(ModelForm):
    class Meta:
        model = gallery
        fields = '__all__'


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email')         

