from django.http import JsonResponse
from django.shortcuts import render, redirect
from sales.models import Comments
from django.contrib.auth.models import User
from editor.models import TShirts
from django.core.mail import send_mail
from django.conf import settings


def index(request, pk):
    if request.method == 'POST':
        name = request.user.username
        user = request.user
        if name == '':
            name_user = request.POST.get('name_user')
            email_user = request.POST.get('email_user')
        else:
            email_user = user.email
            name_user = name
        price = TShirts.objects.get(id=pk).price
        subject = 'Mailing on brushka.ru'
        my_email = settings.EMAIL_HOST_USER
        to_list = [email_user]
        message = 'Hello,' + name_user + '!\nYou buy tshirts. Price: ' + str(price) + '$.\nLink T-Shirt: '\
                  + TShirts.objects.get(id=pk).link_TShirts + '\nThank you!'
        send_mail(subject, message, my_email, to_list, fail_silently=True)
        return redirect('home_page_index')
    else:
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
