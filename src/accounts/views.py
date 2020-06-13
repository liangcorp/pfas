from django.shortcuts import render, redirect

from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, PasswordResetView

from .forms import LoginForm, SignupForm, CustomPasswordChangeForm

User = get_user_model()


def login_user(request):
    """
        Use function view to get better control over form.errors and
    remember_me checkbox
    """
    login_form = LoginForm()

    context = {
        "login_form": login_form
    }

    if not request.user.is_authenticated:
        if request.method == "POST":
            login_form = LoginForm(data=request.POST)
            print(login_form)
            if login_form.is_valid():
                email = login_form.cleaned_data['email']
                password = login_form.cleaned_data['password']
                remember_me = login_form.cleaned_data.get("remember_me")

                if not remember_me:
                    request.session.set_expiry(0)
                    request.session.modified = True

                user = authenticate(request,
                                    email=email,
                                    password=password)

                if user is not None:
                    login(request, user)
                    # Redirect to a success page.
                    return redirect('/app/')
                else:
                    # Return an 'invalid login' error message.
                    return render(request, "accounts/login.html", context)
            else:
                context = {
                    "login_form": login_form
                }
                return render(request, "accounts/login.html", context)

        return render(request, "accounts/login.html", context)
    else:
        return redirect('app:appcenter')


class AccountsLogoutView(LogoutView):
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


class AccountsPasswordResetView(PasswordResetView):
    template_name = "forgot-password.html"


# Reset password with function
def password_reset(request):
    context = {}
    return render(request, 'accounts/forgot-password.html', context)


def password_reset_done(request):
    pass


def reset(request):
    pass


def reset_done(request):
    pass


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
