from django.conf.urls import url
from editor.models import TShirts
from django.views.generic import DetailView
from .views import index

urlpatterns = [
    # url('^(?P<pk>\d+)$', DetailView.as_view(model=TShirts, template_name='sales.html')),
    url('^(?P<pk>\d+)$', index, name='comments')
]
