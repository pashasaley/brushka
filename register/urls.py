from django.urls import path
from register import views

urlpatterns = [
    path('', views.register, name='index'),
    # path('register/', views.register),
]
