from django.shortcuts import render


# Create your views here.
def get_landing_page(request):
    context = {}
    return render(request, 'landing/landing.html', context)
