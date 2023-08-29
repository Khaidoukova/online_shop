from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.core.mail import send_mail

from catalog.forms import StyleFormMixin
from config import settings
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "phone", "country", "avatar", "password1", "password2"]


class UserProfileForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ["email", "password", "first_name", "last_name", "phone", "country", "avatar"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()