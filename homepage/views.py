from django.shortcuts import render
from register.forms import CustomUserCreationForm


def index(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        mail = f.email
        return render(request, 'home_page/home_page.html', {'mail': mail})
    return render(request, 'home_page/home_page.html')
