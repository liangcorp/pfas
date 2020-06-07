from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required


def login_user(request):
    template_name = "accounts/login.html"

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.

    else:
        # Return an 'invalid login' error message.
        context = {}
        return render(request, template_name, context)


@login_required
def logout_user(request):
    logout(request)


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
