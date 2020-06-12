from django.shortcuts import render

# from profiles.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def get_profile(request):
    print(request.session.get('_auth_user_id'))
    user = User.objects.get(id=request.session.get('_auth_user_id'))
    print(user)
    context = {
        'user': user
    }

    return render(request, "profiles/profile.html", context)
