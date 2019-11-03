from django.shortcuts import render
from editor.models import TShirts


def index(request):
    if request.method == 'POST':
        id_ts = request.POST['id']
        ts = TShirts.objects.get(id=id_ts)
        ts.delete()
    username = request.user.username
    queryset = TShirts.objects.filter(username=username)
    return render(request, 'private_office.html', {'queryset': queryset})
