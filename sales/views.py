from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from sales.models import Comments
from django.contrib.auth.models import User
from editor.models import TShirts


def index(request):
    return render(request, 'sales.html')


def create_comment(request):
    id_ts = request.POST.get('id_ts')
    comment = request.POST.get('inputComment')
    id_user = request.POST.get('id_user')
    tshirts = TShirts.objects.get(id=id_ts)
    user = User.objects.get(id=id_user)
    comment_ts = Comments(id_ts=tshirts, id_user=user, comment=comment)
    comment_ts.save()
    add_comment = [{'username': user.username, 'comment': comment_ts.comment}]
    return JsonResponse(add_comment, safe=False)


def search_comment(request):
    comments = Comments.objects.all().order_by('id')
    # comment = Comments.objects.get(id=1)
    data = []
    for comment in comments:
        d = {'username': comment.id_user.username, 'comment': comment.comment}
        data.append(d)
    return JsonResponse(data, safe=False)
