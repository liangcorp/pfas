from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Row, Column
# from django.urls import reverse

# from .models import Account


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your Username...'}
        ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Your Password...'}
        ))
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
        max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter Your Username...'}
        ))

    email = forms.EmailField(max_length=50,
                             required=True,
                             )

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
        model = User
        fields = ('username',
                  'email',
                  'password1',
                  'password2', )


"""
class PasswordChangeForm(authforms.PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field("old_password",
                  placeholder="Enter old password",
                  autofocus=""),
            Field("new_password1", placeholder="Enter new password"),
            Field("new_password2", placeholder="Enter new password (again)"),
            Submit("pass_change", "Change Password", css_class="btn-warning"),
        )


class PasswordResetForm(authforms.FriendlyPasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field("email", placeholder="Enter email", autofocus=""),
            Submit("pass_reset", "Reset Password", css_class="btn-warning"),
        )


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
