from django.urls import path
from homepage import views

urlpatterns = [
    path('', views.index, name='home_page_index'),
    # path('register/', views.register),
]