from django.urls import path
from .views import index, edit
from django.conf.urls import url


urlpatterns = [
    path('', index, name='private_office'),
    url('edit/(?P<pk>\d+)$', edit, name='edit')
]
