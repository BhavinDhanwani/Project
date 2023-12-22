"""
URL configuration for iplinfo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from iplteams import views

urlpatterns = [
    path('', views.home, name='home'),
    path('CSK', views.CSK, name='CSK'),
    path('DC', views.DC, name='DC'),
    path('GT', views.GT, name='GT'),
    path('KKR', views.KKR, name='KKR'),
    path('LSG', views.LSG, name='LSG'),
    path('MI', views.MI, name='MI'),
    path('PBKS', views.PBKS, name='PBKS'),
    path('RCB', views.RCB, name='RCB'),
    path('RR', views.RR, name='RR'),
    path('SRH', views.SRH, name='SRH'),
]
