from django import forms
from django.core.exceptions import ValidationError

from user.models import UserModel


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'placeholder': 'username'
    }))
    password = forms.CharField(max_length=16, min_length=6, widget=forms.PasswordInput())


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=3, widget=forms.TextInput(attrs={
        'placeholder': 'Your username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'youremailname@gmail.com'
    }))
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25, required=False)
    password = forms.CharField(max_length=16, min_length=6, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=16, min_length=6, widget=forms.PasswordInput)

    def clean_confirm_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            raise ValidationError('The passwords are not the same!')
        return self.cleaned_data


class UserProfileForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=3, widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)


class ImageUploadForm(forms.Form):
    user_img = forms.ImageField(widget=forms.FileInput())