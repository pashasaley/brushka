from django.conf.urls import url

from .views import index


urlpatterns = [
    url('^(?P<pk>\d+)$', index, name='comments'),
]
