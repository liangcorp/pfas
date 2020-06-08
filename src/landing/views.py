from django.shortcuts import render


# Create your views here.
def get_landing_page(request):
    context = {}
    return render(request, 'landing/landing.html', context)


def page_not_found_404(request, exception):
    context = {}
    return render(request, 'landing/404.html', context)
