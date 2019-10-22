from django.shortcuts import render


def index(request):
    return render(request, '../templates/home_page.html')
