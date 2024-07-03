#from django.conf.urls import url

from django.urls import path

from . import views

urlpatterns = [

    path('inicio', views.index, name='inicio'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('libro1', views.libro1, name='libro1'),
    path('libro2', views.libro2, name='libro2'),
    path('libro3', views.libro3, name='libro3'),
    path('portadas', views.portadas, name='portadas'),
    
]