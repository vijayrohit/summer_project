from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def registration(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})