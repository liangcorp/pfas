from django.shortcuts import render, redirect

from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LogoutView

from .forms import LoginForm, SignupForm
# from django.conf import settings


# Use function view to get better control over form.errors and remember_me
def login_user(request):
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


"""
# Not used due to log in will cause a page refresh
# which removes the login error.

class AccountsLoginView(LoginView):
    template_name = "accounts/login.html"
    form_class = LoginForm
    form = LoginForm()
    next = 'app:appcenter'
    extra_context = {
                        "login_form": form
    }

    def form_valid(self, form):
        redirect = super().form_valid(form)
        remember_me = form.cleaned_data.get("remember_me")
        print(remember_me)
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True

        return redirect
"""


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


"""
class AccountsUserCreationForm(UserCreationForm):
    template_name = 'accounts/register.html'
    form_class = LoginForm
    form = LoginForm()
"""


def redirect_to_app(request):
    # request.session.set_expiry(request.GET.get('remember_me'))
    return redirect('app:appcenter')


@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
        else:
            ...


@login_required
def password_change_done(request):
    pass


def password_reset(request):
    context = {}
    return render(request, 'accounts/forgot-password.html', context)


def password_reset_done(request):
    pass


def reset(request):
    pass


def reset_done(request):
    pass
