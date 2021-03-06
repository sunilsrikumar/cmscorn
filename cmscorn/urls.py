"""cmscorn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.flatpages import views
from contact import views as contact_views
from django.views.generic.base import TemplateView

from newsletter.views import subscribe

urlpatterns =[
    url(r'^$', views.flatpage, {'url': '/home/'}, name='home'),
	url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^blog/', include('blog.urls')),
	# url(r'^about/$', views.flatpage, {'url': '/about/'}, name='about'), # enable to have custom url for flatpage
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('registration.urls')),
    url(r'^users/', include('django.contrib.auth.urls')),
    url(r'^', include('contact.urls')),
    url(r'^subscribe/', subscribe, name = "subscribe"),
]
