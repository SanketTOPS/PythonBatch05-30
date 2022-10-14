from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.index),
    path('confirm/',views.confirm,name='confirm'),
    path('updatedata/',views.updatedata),
    path('deletedata/<int:id>',views.deletedata),
]
