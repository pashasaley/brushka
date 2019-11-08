from django.shortcuts import render
from django.contrib.auth.models import User


def admin_page(request):
    users = User.objects.all()
    return render(request, 'admin_page.html', {'users': users})
