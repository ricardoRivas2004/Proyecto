#from django.conf.urls import url

from django.urls import path

from . import views

urlpatterns = [

    path('inicio', views.index, name='inicio'),
    path('libro1', views.libro1, name='libro1'),
    path('libro2', views.libro2, name='libro2'),
    path('libro3', views.libro3, name='libro3'),
    path('libro4', views.libro4, name='libro4'),
    path('libro5', views.libro5, name='libro5'),
    path('libro6', views.libro6, name='libro6'),
    path('libro7', views.libro7, name='libro7'),
    path('libro8', views.libro8, name='libro8'),
    path('portadas', views.portadas, name='portadas'),
    path('crud', views.crud, name='crud'),
    path('librosAdd', views.librosAdd, name='librosAdd'),
    path('libro_del/<str:pk>', views.libros_del, name='libro_del'),
    path('libros_findEdit/<str:pk>', views.libros_findEdit, name='libros_findEdit'),
    path('librosUpdate', views.librosUpdate, name='librosUpdate'),
    path("register/", views.registro, name="register"),
]