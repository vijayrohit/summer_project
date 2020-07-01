from django.shortcuts import render



def home(request):
    return render(request, 'delivery/home.html')


def about(request):
    return render(request, 'delivery/about.html', {'title': 'About'})
