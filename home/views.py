from django.shortcuts import render, redirect

from Global import Global


# Create your views here.
def html(request):
    info = Global.saveHistory(request, "login")
    return render(request,"home.html",{"info":info[1]})