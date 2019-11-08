from django.urls import path
from .views import admin_page, delete_user, create_admin, block_user

urlpatterns = [
    path('', admin_page, name='admin_page'),
    path('delete/', delete_user, name='delete_user'),
    path('create_admin/', create_admin, name='create_admin'),
    path('block_user/', block_user, name='block_user'),
]
