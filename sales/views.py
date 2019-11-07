from django.http import JsonResponse
from django.shortcuts import render
from sales.models import Comments
from django.contrib.auth.models import User
from editor.models import TShirts


def index(request, pk):
    tshirts = TShirts.objects.get(id=pk)
    comments = Comments.objects.filter(id_ts=pk).order_by('-id')
    return render(request, 'sales.html', {'comments': comments, 'tshirts': tshirts})


def create_comment(request):
    id_ts = request.POST.get('id_ts')
    comment = request.POST.get('inputComment')
    id_user = request.POST.get('id_user')
    tshirts = TShirts.objects.get(id=id_ts)
    user = User.objects.get(id=id_user)
    comment_ts = Comments(id_ts=tshirts, id_user=user, comment=comment)
    comment_ts.save()
    add_comment = [{'username': user.username, 'comment': comment_ts.comment, 'id': comment_ts.id}]
    return JsonResponse(add_comment, safe=False)


def search_comment(request):
    id_ts = request.GET.get('id_ts')
    comments = Comments.objects.filter(id_ts=id_ts).order_by('-id')
    data = []
    for comment in comments:
        d = {'username': comment.id_user.username, 'comment': comment.comment, 'id': comment.id}
        data.append(d)
    return JsonResponse(data, safe=False)
