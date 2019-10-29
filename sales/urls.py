from django.conf.urls import url
from django.urls import path
from editor.models import TShirts
from django.views.generic import DetailView

urlpatterns = [
    url('^(?P<pk>\d+)$', DetailView.as_view(model=TShirts, template_name='sales.html')),
]
