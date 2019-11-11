from django.shortcuts import render, redirect
from editor.models import TShirts, Tags, save_tags
from furl import furl
from django.contrib.auth.models import User
from django.http import HttpResponse


def index(request):
    path = request.get_full_path()
    f = furl(path)
    if path == '/private_office/':
        username = request.user.username
    else:
        user = User.objects.get(id=f.args['user'])
        username = user.username
    if request.method == 'POST':
        id_ts = request.POST['id']
        ts = TShirts.objects.get(id=id_ts)
        ts.delete()
    queryset = TShirts.objects.filter(username=username)
    return render(request, 'private_office.html', {'queryset': queryset})


def edit(request, pk):
    global string
    if request.method == 'POST':
        tshirts = TShirts.objects.get(id=pk)
        name = request.POST.get('name')
        tags_t = Tags.objects.filter(id_ts=pk)
        price = request.POST.get('price_t')
        description = request.POST.get('description_t')
        string_tags = request.POST.get('tags_t')
        tags = string_tags.split(' ')
        if tshirts.name_TShirts != name:
            tshirts.name_TShirts = name
        if tshirts.price != price:
            tshirts.price = price
        if tshirts.description != description:
            tshirts.description = description
        tags_t.delete()
        save_tags(tags, tshirts)
        tshirts.save()
        return redirect('private_office')
    tshirts = TShirts.objects.get(id=pk)
    tags = Tags.objects.filter(id_ts=pk)
    return render(request, 'edit.html', {'tshirts': tshirts, 'tags': tags})
