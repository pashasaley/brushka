import random
from register.models import Users, get_id, parse_url
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            key = str(random.getrandbits(32))
            f.save(key)
            mail = f.cleaned_data["email"]
            subject = 'Mailing on brushka.ru'
            message = 'http://127.0.0.1:8000/register/activate?kod=' + key
            my_email = settings.EMAIL_HOST_USER
            to_list = [mail]

            send_mail(subject, message, my_email, to_list, fail_silently=False)

            return redirect('home_page_index')

    else:
        f = CustomUserCreationForm()

    return render(request, 'register/register.html', {'form': f}, )


def activate(request):
    global u
    path = request.get_full_path()
    activate_key = parse_url(path, 'kod')
    id_user = get_id(activate_key)
    for u in Users.objects.filter(id=id_user):
        u.is_active = True
        u.save()
    return redirect('home_page_index')
