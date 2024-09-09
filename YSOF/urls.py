"""
URL configuration for YSOF project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.staticfiles.views import serve
from django.urls import path, re_path
from django.conf.urls import include
from django.conf.urls.static import static

from . import settings
from Home.views import HomeView
from User.views import UserView,LoginView,UserInfoView,UserAvatarView,SaveProfileView
from TagArticle.views import SearchTagView,SearchSingleTagView,CreateTagView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('user/', UserView.as_view(), name='user'),
    path('user/login/', LoginView.as_view(), name='login'),
    path('user/userinfo/', UserInfoView.as_view(), name='userinfo'),
    path('user/useravatar/', UserAvatarView.as_view(), name='useravatar'),
    path('user/saveprofile/', SaveProfileView.as_view(), name='saveprofile'),
    path('tags/searchtags/', SearchTagView.as_view(), name='searchtags'),
    path('tags/searchtag/', SearchSingleTagView.as_view(), name='searchtag'),
    path('tags/createtag/', CreateTagView.as_view(), name='createtag'),
    path('home/', include('Home.urls')),
    #re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)