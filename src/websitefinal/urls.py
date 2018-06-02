"""websitefinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from checkout import views as checkout_views
from contact import views as contact_views
from dataVisualization import views as data_visual
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from profiles import views as profiles_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', profiles_views.home.as_view(), name='home'),
    path('home/', profiles_views.home.as_view(), name='home'),
    path('diagrams/', data_visual.Diagrams.as_view(), name='diagrams'),
    path('about/', profiles_views.about.as_view(), name='about'),
    path('profile/', profiles_views.userProfile.as_view(), name='profile'),
    path('contact/', contact_views.contact.as_view(), name='contact'),
    path('checkout/', checkout_views.checkout.as_view(), name='checkout'),
    path('accounts/', include('allauth.urls')),
    path('profile/edit/', profiles_views.EditUser.as_view(), name='account_update'),
    path('diagrams/amazon', data_visual.AMZN.as_view(), name='amazon'),
    path('diagrams/apple', data_visual.APPL.as_view(), name='apple'),
    path('diagrams/alibaba', data_visual.BABA.as_view(), name='alibaba'),
    path('diagrams/bitcoin', data_visual.BTC_USD.as_view(), name='bitcoin'),
    path('diagrams/facebook', data_visual.FB.as_view(), name='facebook'),
    path('diagrams/microsoft', data_visual.MSFT.as_view(), name='microsoft'),
    path('diagrams/samsung', data_visual.SSNLF.as_view(), name='samsung'),
    path('diagrams/twitter', data_visual.TWTR.as_view(), name='twitter'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
