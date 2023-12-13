from django.urls import path, include

from cosmiosfs.views import home

urlpatterns = [
    
    path('homefonksiyonunugöster/', home),
   
]