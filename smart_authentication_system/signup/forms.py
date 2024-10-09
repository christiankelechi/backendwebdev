from django import forms
from django.contrib.auth.models import User
from signup.models import ClassList
class RegistrationForm(forms.ModelForm):
    class Meta:
        model=ClassList
        fields=['first_name']

class UserForm(User):
    class Meta:
        model=User
        fields="__all__"