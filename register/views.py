from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.http import HttpResponseRedirect


# ...
def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        print(f.as_table())
        if f.is_valid():
            f.save()
            return redirect('index')

    else:
        f = CustomUserCreationForm()

    return render(request, 'register/register.html', {'form': f})


def index(request):
    return HttpResponseRedirect('/')

