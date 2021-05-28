from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index1.html', views.pro, name='index1'),
    path('index2.html', views.exp, name='index2'),
    path('index3.html', views.edu, name='index3'),
    path('index4.html', views.skl, name='index4'),
    path('index5.html', views.crs, name='index5'),
    path('index6.html', views.ext, name='index6'),
    path('index7.html', views.prs, name='index7'),
]