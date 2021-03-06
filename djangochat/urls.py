"""djangochat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib.auth import views as auth_views

from chat.views import ChatRoomsListView, signup


urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),  # The base django login view
    url(r'^logout/$', auth_views.logout, name='logout'),  # The base django logout view
    url(r'^signup/$', signup, name='signup'),  # The base django logout view
    url(r'^admin/', admin.site.urls),
    url(r'^', include('chat.urls')),
    url(r'^$', ChatRoomsListView.as_view(), name='homepage'),  # The start point for index view)

]
