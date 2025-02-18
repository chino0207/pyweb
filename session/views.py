import json
import time

from django.http import HttpResponse
from django.shortcuts import render, redirect
import mysql.connector as mysql
from Global import Global
from Global import Global
chance=3


# Create your views here.
def login(request):
    info=Global.saveHistory(request,"login")
    if "loginCount" in request.session and request.session["loginCount"]>=chance:
        return redirect("/reject")
    return render(request,"login.html",{"info":info[1]})

def logout(request):
    if 'userAccount' in request.session:
        del request.session["userAccount"]
    return redirect("/")

def login_process(request):
    if "loginCount" in request.session and request.session["loginCount"]>=chance:
        return redirect("/reject")
    userAccount=request.POST["userAccount"]
    userPassword=request.POST["userPassword"]
    print(userAccount,userPassword)
    conn=mysql.connect(
        host=Global.dbHost,
        user=Global.dbAccount,
        password=Global.dbPassword,
        database=Global.db,
        charset = 'utf8mb4',
        collation='utf8mb4_unicode_ci'
    )
    cursor=conn.cursor()
    #cmd=f"select * from member_name where userAccount='{userAccount}' and userPassword='{userPassword}'"
    #cursor.execute(cmd)
    cmd = "SELECT * FROM member_name WHERE userAccount = %s AND userPassword = %s"
    cursor.execute(cmd, (userAccount, userPassword))
    rs=cursor.fetchall()
    for r in rs:
        print(r)
    conn.close()
    if len(rs)>0:
        request.session['userAccount']=userAccount
        if "currentPage" in request.session:
            return redirect(request.session["currentPage"])
        else:
            return redirect("/")
    else:
        if "loginCount" not in request.session:
            request.session["loginCount"]=1
        else:
            request.session["loginCount"]+=1

        time.sleep(1)
        if request.session["loginCount"]>=chance:
            return redirect("/reject")
        return render(request,'login.html',{"login":"error"})
#    cursor=conn.cursor()
#    cmd="select * from member_name"
#    cursor.execute(cmd)
#    rs=cursor.fetchall()
#    for r in rs:
#        print(r)

 #   return HttpResponse()

def check_session(request):
    session={"session":"ok"}
    if "userAccount" not in request.session:
        session["session"]="error"
    return HttpResponse(json.dumps(session),content_type="application/json")

def reject(request):
    return render(request,"reject.html")