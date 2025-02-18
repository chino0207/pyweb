"""
URL configuration for pyweb project.

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
from django.urls import path
import first
import views
import home.views as home
from tools import views as tools
from gallery import views as gallery
from travel import views as travel
from session import views as session
from solar import views as solar
from upload import views as upload
urlpatterns = [
    path('admin/', admin.site.urls),
    path("first.html",first.html),
    path("second/",views.html),
    path("third.html",views.third),
    path("",home.html),
    path("tools/",tools.html),

    path("gallery/",gallery.html),
    path("gallery/thumb/",gallery.thumb),
    path("gallery/thumb_doing/",gallery.thumb_doing),
    path("gallery/listThumbDir", gallery.listThumbDir),
    path("gallery/ai_detect", gallery.ai_detect),


    path("travel/",travel.html),
    #path("travel_menu/", travel.map_menu),
    #path("travel_route/", travel.route),
    path("login/",session.login),
    path("logout/",session.logout),
    path("login_process/",session.login_process),
    path("check_session/",session.check_session),
    path("reject/",session.reject),
    path("solar/",solar.html),
    path("upload/photo_form/",upload.photo_form),
    path("upload/photo_process/",upload.photo_process),


]
