
from django.shortcuts import render, redirect

from Global import Global


def html(request):
    info = Global.saveHistory(request, "login")
    request.session["currentPage"] = "/travel"
    if 'userAccount' not in request.session:
        return redirect("/login")
    return render(request,"travel.html",{"info":info[1]})
