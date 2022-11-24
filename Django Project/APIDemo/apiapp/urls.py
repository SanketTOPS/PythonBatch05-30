from django.contrib import admin
from django.urls import path,include
from apiapp import views

urlpatterns = [
   path('getalldata/',views.getalldata),
   path('getstid/<int:id>/',views.getstid),
   path('deletedata/<int:id>/',views.deletedata),
   path('savedata/',views.savedata),
   path('updatedata/<int:id>/',views.updatedata),
]
