from django.shortcuts import render, redirect

from django.contrib.auth import (
    update_session_auth_hash,
    login,
    logout,
    authenticate
)

from django.contrib.auth.decorators import login_required

from .forms import (
    CustomPasswordChangeForm
)

from allauth.account.forms import LoginForm
from allauth.account.views import (
    LoginView,
    SignupView,
    EmailView,
    ConfirmEmailView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordResetFromKeyView,
)


def login_user(request):
    """Use function view to get better control over form.errors and
    remember_me checkbox.
    """
    login_form = LoginForm()

    if not request.user.is_authenticated:
        if request.method == "POST":
            login_form = LoginForm(data=request.POST)

            if login_form.is_valid():
                username = login_form.cleaned_data['login']
                password = login_form.cleaned_data['password']
                remember_me = login_form.cleaned_data.get("remember_me")

                user = authenticate(request,
                                    username=username,
                                    password=password)

                if not remember_me:
                    request.session.set_expiry(0)
                    request.session.modified = True

                if user is not None:
                    login(request, user)
                    # Redirect to a success page.
                    return redirect('app:appcenter')

    else:
        return redirect('app:appcenter')

    context = {
        "login_form": login_form
    }

    return render(request, "accounts/login.html", context)


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    success_url = "/app/"


def logout_user(request):
    logout(request)
    return redirect('accounts:account_login')


class CutomeSignupView(SignupView):
    """Use custom template for the signup form.
    """
    template_name = 'accounts/signup.html'


class CustomEmailView(EmailView):
    template_name = 'accounts/email.html'


class CustomConfirmEmailView(ConfirmEmailView):
    """View for verifying new user account.
    This will show after the new user click the verification
    link in their email.
    """
    template_name = "accounts/email_confirm.html"


def confirm_email_sent(request):
    """Notifying the new user that an account verification email
    had been sent to their email addresses.
    """
    context = {}
    return render(request, "accounts/verification_email_sent.html", context)


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"


class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset_confirm.html'


class CustomPasswordResetFromKeyView(PasswordResetFromKeyView):
    template_name = "accounts/password_reset_from_key.html"


class CustomPasswordChangeView(PasswordChangeView):
    template_name = "accounts/change-password.html"


@login_required
def password_change(request):
    password_change_form = CustomPasswordChangeForm()

    context = {
        "password_change_form": password_change_form
    }

    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
        else:
            context = {
                "password_change_form": password_change_form
            }
        return render(request, "accounts/change-password.html", context)

    return render(request, "accounts/change-password.html", context)


@login_required
def password_change_done(request):
    password_change_form = CustomPasswordChangeForm()

    context = {
        "password_change_form": password_change_form
    }

    if request.method == 'POST':
        return render(request, "accounts/change-password.html", context)
