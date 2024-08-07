from django.shortcuts import render, redirect
from django.views import View
from App.models import *

class Home(View):
    def get(self, request):
        return render(request, "home.html")
    def get(self, request):
        return render(request, "home.html")
    

