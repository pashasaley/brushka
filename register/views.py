import random
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import CustomUserCreationForm
from django.http import HttpResponseRedirect


def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)

        if f.is_valid():

            f.save()
            mail = f.cleaned_data["email"]
            key = str(random.getrandbits(32))
            subject = 'Mailing on brushka.ru'
            message = 'Your activate key is\n' + key
            my_email = settings.EMAIL_HOST_USER
            to_list = [mail]

            send_mail(subject, message, my_email, to_list, fail_silently=True)

            return redirect('index')

    else:
        f = CustomUserCreationForm()

    return render(request, 'register/register.html', {'form': f}, )


def index(request):
    return HttpResponseRedirect('/')

