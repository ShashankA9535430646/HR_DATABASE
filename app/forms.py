from django import forms
from .models import model1
from django.contrib.auth.models import User

class form1(forms.ModelForm):
    class Meta:
        model = model1
        fields = '__all__'

class Registration(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','password')
