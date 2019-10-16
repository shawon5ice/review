from django import forms
from django.core import validators
from .models import User
# def check_for_s(value):
#   if value[0].lower()!='s':
#     raise forms.ValidationError("Name doesn't start with s")

class my_form(forms.Form):
  name = forms.CharField() #validators=[check_for_s]    calling own validators
  email = forms.EmailField()
  verify_email = forms.EmailField(label='Enter your email again'+"\n")
  text = forms.CharField(widget=forms.Textarea)
  botcatcher = forms.CharField(required=False,
                               widget=forms.HiddenInput,
                               validators=[validators.MaxLengthValidator(0)])
  def clean(self):
    all_clean_data = super().clean()
    email = all_clean_data['email']
    vemail = all_clean_data['verify_email']

    if email != vemail:
      raise forms.ValidationError("Must match both email!")

  # def clean_botcatcher(self):
  #   botcatcher = self.cleaned_data['botcatcher']
  #   if len(botcatcher)>0:
  #     raise forms.ValidationError("I got you Mr.Robot")
  #   return botcatcher


class User(forms.ModelForm):
  class Meta():
    model = User
    fields = '__all__'