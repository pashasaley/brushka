from django.shortcuts import render
from editor.models import TShirts
from furl import furl
from django.contrib.auth.models import User


def index(request):
    f = furl(request.get_full_path())
    id_user = f.args['user']
    if id_user:
        user = User.objects.get(id=id_user)
        username = user.username
    else:
        username = request.user.username
    if request.method == 'POST':
        id_ts = request.POST['id']
        ts = TShirts.objects.get(id=id_ts)
        ts.delete()
    # username = request.user.username
    queryset = TShirts.objects.filter(username=username)
    return render(request, 'private_office.html', {'queryset': queryset})
