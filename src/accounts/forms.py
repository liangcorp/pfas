from django.contrib.auth.forms import AuthenticationForm
from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, HTML, Field
# from django.contrib.auth import forms as authforms
# from django.urls import reverse

from .models import Account


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
                            attrs={'placeholder': 'Enter Your Username...'}
                            ))
    password = forms.CharField(widget=forms.PasswordInput(
                            attrs={'placeholder': 'Enter Your Password...'}
                            ))

    class Meta:
        model = Account
        fields = [
            'username',
            'password'
        ]


"""
    email = forms.CharField(widget=forms.TextInput(
                            attrs={'placeholder': 'Enter Your Email...'}
                            ))

    password = forms.CharField(widget=forms.PasswordInput())

    remember_me = forms.BooleanField(required=False, initial=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.fields["username"].widget.input_type = "email"  # ugly hack

        self.helper.layout = Layout(
            Field("username",
                  placeholder="Enter Username...",
                  css_class="form-control form-control-user",
                  autofocus="",),

            Field("password",
                  placeholder="Password",
                  css_class="form-control form-control-user",),

            HTML(
                '<a href="{}">Forgot Password?</a>'.format(
                    reverse("password_reset")
                )
            ),

            Field("remember_me", css_class="form-control form-control-user",),

            Submit("sign_in",
                   "Log in",
                   css_class="btn btn-primary btn-user btn-block"),
        )
"""


"""
class SignupForm(authforms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["email"].widget.input_type = "email"  # ugly hack

        self.helper.layout = Layout(
            Field("email", placeholder="Enter Email", autofocus=""),
            Field("name", placeholder="Enter Full Name"),
            Field("password1", placeholder="Enter Password"),
            Field("password2", placeholder="Re-enter Password"),
            Submit("sign_up", "Sign up", css_class="btn-warning"),
        )


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
