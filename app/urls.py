from django.urls import path
from .views import jasurbek,sahifa2class,sahifaclass,sahifa3class,bosh,Boshsahifa


urlpatterns=[
    path('',jasurbek,name='jasurbek'),
    path('sahifa1',sahifaclass.as_view(),name='a'),
    path('sahifa2',sahifa2class.as_view(),name='b'),
    path('sahifa3',sahifa3class.as_view(),name='c'),
    path('admin',bosh.as_view(),name='d'),
    path('malumot',Boshsahifa.as_view(),name='as')


]

