"""core URL Configuration

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
from vege.views import *
from django.conf import settings
from django.conf.urls.static import static
import home.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('textsearch/', include('textsearch.urls')),
    path('recepies', recepies, name='recepies'),
    path('delete-recepies/<id>/', delete_recepies, name='delete_recepies'),
    path('update-recepies/<id>/', update_recepies, name='update_recepies'),
    path('login/', login_page, name='login_page'),
    path('register/', register, name="register"),
    path('logout/', logout_user, name='logout_user'),
    path('djmiddleware/', include('djmiddleware.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    
    path('elastic_search/', include('elasticsearch_app.urls')),
    path('scrapper/', include('scraper.urls')),
    path('rabbit-mq-app/', include('rabbit_mq_app.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)