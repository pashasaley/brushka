from django.shortcuts import render
from editor.models import TShirts, Tags


def add_tags(request):
    if request.method == 'POST':
        tag = request.POST['tag']
        queryset = TShirts.objects.filter(tags__tag=tag)
        tags = Tags.objects.distinct('tag')
        return render(request, 'home_page.html', {'queryset': queryset, 'tags': tags})
    else:
        queryset = TShirts.objects.all().order_by('-id')[:9]
        tags = Tags.objects.distinct('tag')
        return render(request, 'home_page.html', {'queryset': queryset, 'tags': tags})
