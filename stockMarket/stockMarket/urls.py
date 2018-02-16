from django.contrib import admin
from django.urls import path
from django.conf.urls import  include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('',include('home.urls') ),
    path('home/',include('home.urls') ),
]
