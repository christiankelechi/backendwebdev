from django import forms
from django.contrib.auth.models import User
from core_root.models import Member
class RegisterForm(forms.Form):
    class Meta:
        model=Member
        fields="__all__"