from django.shortcuts import render
from editor.models import TShirts
from django.http import HttpResponse


def index(request):
    username = request.user.username
    queryset = TShirts.objects.filter(username=username)
    return render(request, 'private_office.html', {'queryset': queryset})
