from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import BlockUser


def admin_page(request):
    users = User.objects.values('username', 'id', 'is_superuser', 'is_staff', 'blockuser__block')
    return render(request, 'admin_page.html', {'users': users})


def delete_user(request):
    id_user = request.POST['id_user_for_delete']
    user = User.objects.get(id=id_user)
    user.delete()
    return redirect('admin_page')


def create_admin(request):
    id_user = request.POST['id_user_for_create']
    user = User.objects.get(id=id_user)
    if user.is_staff:
        if user.is_superuser:
            user.is_staff = False
            user.is_superuser = False
    else:
        user.is_staff = True
        user.is_superuser = True
    user.save()
    return redirect('admin_page')


def block_user(request):
    id_user = request.POST['id_user_for_delete']
    user = BlockUser.objects.get(id_user=id_user)
    if user.block:
        user.block = False
    else:
        user.block = True
    user.save()
    return redirect('admin_page')

