"""batpubs URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView, ListView, DetailView
from publishers.views import (
    PublisherListView,
    PublisherDetailView,
    PublisherCreateView,
    PublisherUpdateView,
    CategoryListView,
    PubCategoryListlView,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', PublisherCreateView.as_view(template_name='home.html')),
    url(r'^add/$', PublisherCreateView.as_view()),
    url(r'^category/$', CategoryListView.as_view()),
    url(r'^category/(?P<slug>[\w-]+)/$', PubCategoryListlView.as_view()),
    url(r'^publishers/$', PublisherListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/update/$', PublisherUpdateView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', PublisherDetailView.as_view()),
    url(r'^publishers/category/(?P<slug>[\w-]+)/$', PublisherListView.as_view()),
]
