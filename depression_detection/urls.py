"""depression_detection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path('',views.first),
    path('index',views.index),
    path('reg',views.reg),
    path('register',views.register),
    path('docc',views.docc),
    path('doctor',views.doctor),
    path('guss',views.guss),
    path('guest',views.guest),
    path('viewuser',views.viewuser),
    path('viewpsychiatrist',views.viewpsychiatrist),
    path('viewguestuser',views.viewguestuser),
    path('login/',views.login),
    path('login/addlogin',views.addlogin),
    path('logout/',views.logout),
    path('userdoctor',views.userdoctor),
    path('bookuser/<int:id>',views.bookuser),
    path('bookuser/addbook',views.addbook),
    path('viewappoint',views.viewappoint),
    path('press/<int:id>',views.press),
    path('press/addpres/<int:id>',views.addpres,name="addpres"),
    path('faq',views.faq),
    path('data_submit',views.data_submit),
    path('viewpres',views.viewpres),
    path('feed',views.feed),
    path('addfeed',views.addfeed),
    path('viewfeed',views.viewfeed),
    path('depression',views.depression),
    path('u_result',views.u_result),
    path('viewappointadmin',views.viewappointadmin),
    path('viewpays',views.viewpays),
    path('pay/<int:id>',views.pay),
    path('pay/addpay',views.addpay,name='addpay'),
    path('paid/<int:id>',views.paid,name='paid'),
    path('paid/addpayuser',views.addpayuser,name="addpayuser"),
    path('payss',views.payss),
    path('inss',views.inss),
    path('medii',views.medii),
    path('addmed',views.addmed),
    path('ress',views.ress),

]
