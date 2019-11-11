from django.shortcuts import render
from editor.models import TShirts, get_tags
from admin_page.models import BlockUser
from django.http import HttpResponseForbidden


def add_tags(request):
    if request.method == 'POST':
        tag = request.POST['tag']
        queryset = TShirts.objects.filter(tags__tag=tag)
        tags = get_tags()
        return render(request, 'home_page.html', {'queryset': queryset, 'tags': tags})
    else:
        user = request.user.id
        if user != '':
            if BlockUser.objects.get(id_user=user).block:
                return HttpResponseForbidden()
        queryset = TShirts.objects.all().order_by('-id')[:9]
        tags = get_tags()
        return render(request, 'home_page.html', {'queryset': queryset, 'tags': tags})
