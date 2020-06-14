from django.shortcuts import render, redirect

from django.contrib.auth import (
    update_session_auth_hash,
    get_user_model,
    login,
    authenticate
)

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from .forms import (
    LoginForm,
    SignupForm,
    CustomPasswordChangeForm,
    CustomPasswordResetForm,
    CustomSetPasswordForm
)

User = get_user_model()


def login_user(request):
    """Use function view to get better control over form.errors and
    remember_me checkbox.
    """
    if not request.user.is_authenticated:
        if request.method == "POST":
            login_form = LoginForm(data=request.POST)
            print(login_form)
            if login_form.is_valid():
                email = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                remember_me = login_form.cleaned_data.get("remember_me")

                user = authenticate(request,
                                    email=email,
                                    password=password)

                if not remember_me:
                    request.session.set_expiry(0)
                    request.session.modified = True

                if user is not None:
                    login(request, user)
                    # Redirect to a success page.
                    return redirect('/app/')
            else:

                context = {
                    "login_form": login_form
                }
                return render(request, "accounts/login.html", context)
    else:
        return redirect('app:appcenter')

    login_form = LoginForm()
    print(login_form)
    context = {
        "login_form": login_form
    }

    return render(request, "accounts/login.html", context)


class CustomLogoutView(LogoutView):
    next_page = 'landing:index'


def register(request):
    signup_form = SignupForm()

    context = {
        "signup_form": signup_form,
    }

    if request.method == "POST":
        signup_form = SignupForm(data=request.POST)

        if signup_form.is_valid():
            signup_form.save()

            request.session.set_expiry(0)
            request.session.modified = True

            email = signup_form.cleaned_data.get('email')
            password = signup_form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('/app/')
        else:
            context = {
                "signup_form": signup_form,
            }
            return render(request, 'accounts/register.html', context)

    return render(request, 'accounts/register.html', context)


# Create page that allow users to enter their email address
class CustomPasswordResetView(PasswordResetView):
    template_name = "accounts/forgot-password.html"
    form_class = CustomPasswordResetForm
    form = CustomPasswordResetForm()
    from_email = "noreply@liangcorp.com"
    subject_template_name = "accounts/password_reset_subject.txt"
    email_template_name = "accounts/password_reset_email.html"
    success_url = "/accounts/password_reset/done/"


# Confirm that email had been sent
class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"


# Provide page for users to reset their password
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"
    form_class = CustomSetPasswordForm
    # form = CustomSetPasswordForm()
    success_url = "/accounts/password_reset_complete/"


# Confirm the password had changed
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"


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
