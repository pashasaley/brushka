from django.shortcuts import render
from django.db.models import Q
from editor.models import TShirts


def search(request):
    if request.method == 'POST':
        search_ts = request.POST['search']
        if search_ts:
            queryset = TShirts.objects.filter(Q(name_TShirts__icontains=search_ts) | Q(description__icontains=search_ts) |
                                              Q(tags__tag__icontains=search_ts)).distinct()
            return render(request, 'search.html', {'queryset': queryset})
