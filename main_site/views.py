from django.shortcuts import render

# Create your views here.
def site_home(request):
    return render(request, 'main_site/index.html')