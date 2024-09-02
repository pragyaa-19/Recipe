"""
URL configuration for Project project.

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
from home.views import *
from vege.views import *
from django.conf.urls.static import static
from django.conf import settings
#  for adding media file
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    #routing , binding
    path('', index, name='index'),
    path('pragya/', pragya, name='pragya'),
    path('receipis/', receipis, name='receipis'),
    path('login/', loginpage, name='loginpage'),
    path('log-out/', logout, name='logout'),

    path('register/', register, name='register'),
    path('delete_receipis/<id>', delete_receipis, name='delete_receipis'),
    path('update_receipis/<id>', update_receipis, name='update_receipis'),
    path('admin/', admin.site.urls),
]


#  for adding media file
# RENDIRIND THE MEDIA FILE
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()


