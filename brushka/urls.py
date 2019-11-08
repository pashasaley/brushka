"""brushka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register.views import register, activate
from private_office.views import index
from home_page.views import add_tags
from search.views import search
from sales.views import create_comment, search_comment


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', add_tags, name='home_page_index'),
    path('', include('django.contrib.auth.urls')),
    path('search/', search, name='search'),
    path('private_office/', index, name='private_office'),
    path('register/', register, name='register'),
    path('register/activate/', activate, name='activate'),
    path('editor/', include('editor.urls')),
    path('sales/', include('sales.urls')),
    path('add_comment/', create_comment, name='add_comment'),
    path('search_comment/', search_comment, name='search_comment'),
    path('admin_page/', include('admin_page.urls'))
]
