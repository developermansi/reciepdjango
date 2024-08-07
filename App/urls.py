from django.urls import path
from App.views import *
urlpatterns = [
    path("",Home.as_view(),name="home"),
    ]
    
