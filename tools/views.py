
from django.shortcuts import render, redirect

from Global import Global


def html(request):
    info = Global.saveHistory(request, "login")
    request.session["currentPage"] = "/tools"
    if 'userAccount' not in request.session:
        return redirect("/login")
    return render(request,"tools.html",{"info":info[1]})