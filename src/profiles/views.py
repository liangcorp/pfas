from django.shortcuts import render

# from profiles.models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .models import Profile

User = get_user_model()


# Create your views here.
@login_required
def get_profile(request):
    user = User.objects.get(id=request.session.get('_auth_user_id'))

    profile = Profile.objects.get(id=request.session.get('_auth_user_id'))

    context = {
        'user': user,
        'profile': profile,
    }

    return render(request, "profiles/profile.html", context)
