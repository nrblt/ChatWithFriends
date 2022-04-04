"""friendsWithChat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# import chat.views
from chat.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', registrationPage, name='register'),
    path('login/', loginPage, name='login'),
    path('allusers', allUsersPage, name='allusers'),
    path('', mainPage, name='main'),
    path('logout/', logoutPage, name='logout'),
    path('addfriend/<str:pk>/', addFriend, name='addfriend'),
    path('requestfriend/<str:pk>/', requestFriend, name='requestfriend'),
    path('listrequests/', listRequestFriend, name='requestlist'),
    path('listfriends/', listFriends, name='friendslist'),
    path('chat/<str:pk>', chatPage, name='chatpage')
]
