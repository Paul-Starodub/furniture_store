from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class UserLoginForm(AuthenticationForm):
    pass
    # username = forms.CharField()
    # password = forms.CharField()
    #
    # class Meta:
    #     model = get_user_model()
    #     fields = ("username", "password")  # it isn't necessary here
