from django.shortcuts import render

# from django.urls import reverse_lazy
# from authtools import views as authviews
# from braces import views as bracesviews
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from assets.models import Asset

User = get_user_model()

# class CheckAuthApp(bracesviews.AnonymousRequiredMixin, authviews.LoginView):
#    failed_url = reverse_lazy("home")


@login_required
# Create your views here.
def appcenter(request):
    latest_asset_list = Asset.objects.order_by('-asset_type')

    context = {
        'latest_asset_list': latest_asset_list
    }
    return render(request, 'appcenter/appcenter.html', context)


def page_not_found_404(request, exception):
    return render(request, '404.html')
