"""
URL configuration for digitalsociety project.

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
from . import views

urlpatterns = [
    path('', views.login, name='loginpage'),
    path('login-evalute', views.login_evalute, name='login-evalute'),
    path('logout', views.logout, name='logout'),
    path('chairman-profile/', views.chairman_profile, name='chairman_profile'),
    path('chairman-change-password/', views.chairman_change_password, name='chairman-change-password'),
    path('chairman-update-profile/', views.chairman_update_profile, name='chairman-update-profile'),
    path('add-member/', views.add_member, name='add-member'),
]
 