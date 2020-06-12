from django.shortcuts import render, redirect

from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LogoutView

from .forms import LoginForm
# from django.conf import settings


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
        return redirect('landing')


"""
class AccountsLoginView(LoginView):
    template_name = "accounts/login.html"
    form_class = LoginForm
    form = LoginForm()
    next = 'app:appcenter'
    extra_context = {
                        "login_form": form
    }
    # print(form)

    def form_valid(self, form):
        redirect = super().form_valid(form)
        remember_me = form.cleaned_data.get("remember_me")
        print(remember_me)
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True

        return redirect

    def form_valid(self, form):
        print(form)
        # get remember me data from cleaned_data of form
        remember_me = form.cleaned_data['remember_me']
        if not remember_me:
            self.request.session.set_expiry(0)  # if remember me is
            self.request.session.modified = True
        return super(AccountsLoginView, self).form_valid(form)
"""


class AccountsLogoutView(LogoutView):
    next_page = 'landing:index'


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


def register(request):
    context = {}
    return render(request, 'accounts/register.html', context)
