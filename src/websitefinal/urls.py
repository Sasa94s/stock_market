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
    path('diagrams/AAPL', data_visual.AAPL.as_view(), name='AAPL'),
    path('diagrams/AMD', data_visual.AMD.as_view(), name='AMD'),
    path('diagrams/FB', data_visual.FB.as_view(), name='FB'),
    path('diagrams/GOOG', data_visual.GOOG.as_view(), name='GOOG'),
    path('diagrams/INTC', data_visual.INTC.as_view(), name='INTC'),
    path('diagrams/MSFT', data_visual.MSFT.as_view(), name='MSFT'),
    path('diagrams/EA', data_visual.EA.as_view(), name='EA'),
    path('diagrams/NVDA', data_visual.NVDA.as_view(), name='NVDA'),
    path('diagrams/RTN', data_visual.RTN.as_view(), name='RTN'),
    path('diagrams/TWTR', data_visual.TWTR.as_view(), name='TWTR'),
    path('diagrams/YHOO', data_visual.YHOO.as_view(), name='YHOO'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
