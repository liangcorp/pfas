# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django import forms
from appuser.models import AppUser
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Row, Column
# from django.urls import reverse

# from .models import Account


class LoginForm(forms.Form):
    """
    Not using AuthenticationForm. This is due to the change from
    authenticating using username to authenticate using email.
    """
    email = forms.EmailField(
        max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter Your Email...'}))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Your Password...'}))

    remember_me = forms.BooleanField(required=False, initial=False)

    class Meta:
        model = AppUser
        fields = [
            'email',
            'password',
            'remember_me',
        ]


class SignupForm(UserCreationForm):
    email = forms.EmailField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter Your Email...'}))

    password1 = forms.CharField(
        min_length=4,
        label='Password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter Your Password...'}
        ))

    password2 = forms.CharField(
        label='Repeat Password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Repeat Your Password...'}
        ))

    class Meta:
        model = AppUser
        fields = ('email',
                  'password1',
                  'password2', )


# PasswordChangeForm
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Current Password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter Your Current Password...',
                   'autofocus': 'autofocus'}))

    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter Your New Password...'}))

    new_password2 = forms.CharField(
        label='Repeat New Password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Repeat Your New Password...'}))

    class Meta:
        model = AppUser
        fields = ('old_password',
                  'new_password1',
                  'new_password2')


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter Your Email...'}))

    class Meta:
        model = AppUser
        fields = ('email')


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter Your New Password...'}))

    new_password2 = forms.CharField(
        label='Repeat New Password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Repeat Your New Password...'}))

    class Meta:
        model = AppUser
        fields = ('new_password1',
                  'new_password2')

    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field("email", placeholder="Enter email", autofocus=""),
            Submit("pass_reset", "Reset Password", css_class="btn-warning"),
        )
    """


"""
class SetPasswordForm(authforms.SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field("new_password1",
                  placeholder="Enter new password",
                  autofocus=""),
            Field("new_password2", placeholder="Enter new password (again)"),
            Submit("pass_change", "Change Password", css_class="btn-warning"),
        )
"""
