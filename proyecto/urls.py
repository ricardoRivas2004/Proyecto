#from django.conf.urls import url

from django.urls import path

from . import views

urlpatterns = [

    path('inicio', views.index, name='inicio'),
    path('libro1', views.libro1, name='libro1'),
    path('libro2', views.libro2, name='libro2'),
    path('libro3', views.libro3, name='libro3'),
    path('portadas', views.portadas, name='portadas'),
    path('crud', views.crud, name='crud'),
    path('librosAdd', views.librosAdd, name='librosAdd'),
    path('libro_del/<str:pk>', views.libros_del, name='libro_del'),
    path('libros_findEdit/<str:pk>', views.libros_findEdit, name='libros_findEdit'),
    path('librosUpdate', views.librosUpdate, name='librosUpdate'),
    path("register/", views.registro, name="register"),
]