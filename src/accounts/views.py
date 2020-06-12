from django.shortcuts import render, redirect

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

from .forms import LoginForm
from django.contrib.auth.views import LoginView, LogoutView


class AccountsLoginView(LoginView):
    template_name = "accounts/login.html"
    form = LoginForm()
    next = 'app'
    extra_context = {
                        "login_form": form
    }
    # redirect_authenticated_user = True


class AccountsLogoutView(LogoutView):
    next_page = 'landing:index'


def redirect_to_app(request):
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


def register(request):
    context = {}
    return render(request, 'accounts/register.html', context)
