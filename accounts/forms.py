from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomeUser, Profile

class CustomUserCreation(UserCreationForm):

    class Meta:
        model = CustomeUser
        fields = ['pelake_mashin', 'password1', 'password2']


class AuthenticationForm(forms.Form):
    pelake_mashin = forms.CharField()
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),)

class CustomUserProfile(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['user','pelake_mashin', 'id_code', 'first_name', 'last_name','phone', 'address']