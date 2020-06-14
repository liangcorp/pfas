from django.contrib.auth.forms import (
    # AuthenticationForm,
    UserCreationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm)
from allauth.account.forms import LoginForm
from django import forms
from django.contrib.auth.models import User


class CustomLoginForm(LoginForm):
    """AuthenticationForm is hacked to using email as label.
    username is set to take email as input.
    """

    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your Username...'}))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Your Password...'}))

    remember_me = forms.BooleanField(required=False, initial=False)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'remember_me',
        ]


class SignupForm(UserCreationForm):
    username = forms.CharField(
        min_length=4,
        label='Username',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Your Username...'}))

    email = forms.EmailField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Your Email...'}))

    password1 = forms.CharField(
        min_length=4,
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter Your Password...'}))

    password2 = forms.CharField(
        label='Repeat Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repeat Your Password...'}))

    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'password1',
                  'password2', )


# PasswordChangeForm
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Current Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter Your Current Password...',
                'autofocus': 'autofocus'}))

    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter Your New Password...'}))

    new_password2 = forms.CharField(
        label='Repeat New Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repeat Your New Password...'}))

    class Meta:
        model = User
        fields = ('old_password',
                  'new_password1',
                  'new_password2')


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Your Email...'}))

    class Meta:
        model = User
        fields = ('email')


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter Your New Password...'}))

    new_password2 = forms.CharField(
        label='Repeat New Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repeat Your New Password...'}))

    class Meta:
        model = User
        fields = ('new_password1',
                  'new_password2')
