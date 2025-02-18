import os.path
from datetime import datetime
from sys import platform

from django.http import HttpResponse
from django.shortcuts import render, redirect

from Global import Global


# Create your views here.
def photo_form(request):
    info=Global.saveHistory(request,"準備上傳圖片")
    request.session["currentPage"]="/upload/photo_form"
    if "userAccount" not in request.session:
        return redirect("/login")
    return render(request,"upload/photo_form.html",{"state":"first","info":info[1]})

def photo_process(request):
    info = Global.saveHistory(request, "準備上傳圖片")
    root="/Users/chino0207/Downloads/images/primitive"
    current=datetime.now()
    yyyy=current.strftime("%Y")
    ymd=current.strftime("%Y%m%d")
    path=os.path.join(root,yyyy,ymd)
    if not os.path.exists(path):
        os.makedirs(path)
        for img in request.FILES.getlist("userFile"):  # Use `getlist()`
            fileName = os.path.join(path, str(img))
            with open(fileName, "wb") as file:
                for data in img.chunks():
                    file.write(data)
    else:
        for img in request.FILES.getlist("userFile"):  # Use `getlist()`
            fileName = os.path.join(path, str(img))
            with open(fileName, "wb") as file:
                for data in img.chunks():
                    file.write(data)


    return render(request, "upload/photo_form.html",{"state":"ok","info":info[1]})
