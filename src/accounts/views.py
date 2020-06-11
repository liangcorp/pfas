from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

from .forms import LoginForm


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
                print(login_form.cleaned_data)
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']

                # user = authenticate(request,
                #                     username=request.POST.get('username'),
                #                     password=request.POST.get('password'))

                user = authenticate(request,
                                    username=username,
                                    password=password)

                # user = authenticate(request, username, password)

                print(username)
                print(password)

                if user is not None:
                    login(request, user)

                    # Redirect to a success page.
                    return redirect('/app/')

                else:
                    # Return an 'invalid login' error message.

                    print("invalid login")
                    return render(request, "accounts/login.html", context)
            else:
                context = {
                    "login_form": login_form
                }
                print(login_form.errors)
                return render(request, "accounts/login.html", context)

        return render(request, "accounts/login.html", context)
    else:
        logout(request)
        return redirect('landing')


@login_required
def logout_user(request):
    logout(request)
    return redirect('landing')


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
