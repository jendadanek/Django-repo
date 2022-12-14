"""chatterbox_project URL Configuration

The `urlpatterns` list routes URLs to views1. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views1
    1. Add an import:  from my_app import views1
    2. Add a URL to urlpatterns:  path('', views1.home, name='home')
Class-based views1
    1. Add an import:  from other_app.views1 import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import accounts.views
import base.views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', base.views.hello),
    path('search/', base.views.search, name = "search"),
    path('room/<id>', base.views.room, name = "room"),
    # path('', base.views.home, name = "home"),
    path('', base.views.Roomsview.as_view(), name ="home"),
    # path('room_create', base.views.room_create, name = "room_create"),
    path('room_create/', base.views.RoomCreateView.as_view(), name='room_create'),
    path('room_update/<pk>', base.views.RoomUpdateView.as_view(), name='room_update'),
    path('room_delete/<pk>', base.views.RoomDeleteView.as_view(), name='room_delete'),
    path('accounts/signup/', accounts.views.SignUpView.as_view(), name='signup'),
    path('accounts/', include("django.contrib.auth.urls")),

]

