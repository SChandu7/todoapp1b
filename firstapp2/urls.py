"""
URL configuration for firstapp2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import home,demo,demo2,nothing,yash,navya
from firstdemoapp2.views import signup_view, login_view, home2,send,get_user_data
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
     path('home/', home2),
    path('demo/', demo),
    path('yash/', yash),
    path('demo/demo/', demo2),
    path('nothing/', nothing),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('send/', send, name='send'),
    path('navya/', navya, name='navya'),
    path('receive', get_user_data, name='get_user_data'),

]
