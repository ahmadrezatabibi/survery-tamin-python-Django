# dappx/forms.py
from django import forms
from dappx.models import UserProfileInfo
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
#  password = forms.CharField(widget=forms.PasswordInput())
 class Meta():
  model = User
  fields = ('username','last_name','password','email')
class UserProfileInfoForm(forms.ModelForm):
 
 class Meta():
  model = UserProfileInfo
  fields = ('portfolio_site','profile_pic')
# class SurveyForm(forms.ModelForm):
# #  password = forms.CharField(widget=forms.PasswordInput())
#  class Meta():
#   model = Survey
#   fields = ('question','value')

