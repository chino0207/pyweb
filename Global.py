from datetime import datetime

import requests
from django.utils.safestring import mark_safe
import mysql.connector as mysql

class Global():
    dbHost="localhost"
    dbAccount="root"
    dbPassword="123456"
    db="cloud"
    @staticmethod
    def saveHistory(request,page):
        x=request.META.get("HTTP_X_FORWARDED_FOR")
        if x:
            ip=x.split(",")[0]
        else:
            ip=request.META.get("REMOTE_ADDR")
        city=""
        country=""
        lat=0
        lng=0
        url="http://ip-api.com/batch?"
        param={"fileds":"status,message,country,countryCode,region,regionName,city,query,lon,lat",
               "lang":"en-US"}
        ip_list=[ip]
        res=requests.post(url=url,params=param, json=ip_list)
        print(res)
        info=res.json()[0]
        if "country" in info:
            country=info["country"]
            city=info["city"]
            lat=info["lat"]
            lng=info["lon"]
        print(info)
        t=datetime.now()
        eventDay=t.strftime("%Y-%m-%d")
        eventTime=t.strftime("%H:%M:%S")
        #if ip not in[127.0.0.1]:

        conn=mysql.connect(host=Global.dbHost,
                           user=Global.dbAccount,
                           password=Global.dbPassword,
                           database=Global.db,
                           charset='utf8mb4',
                           collation='utf8mb4_unicode_ci'
                           )
        if "userAccount" in request.session:
            userAccount=request.session["userAccount"]
        else:
            userAccount=""
        cursor=conn.cursor()
        cmd=f""" 
            insert into history  
            (ip, eventDay,eventTime,page,userAccount,country,city,lng,lat) values (
            "{ip}","{eventDay}","{eventTime}","{page}","{userAccount}","{country}","{city}","{lng}","{lat}"
            )   
        """
        cursor.execute(cmd)
        conn.commit()
        conn.close()

        print("ip is",ip)
        return ip,mark_safe(
        f"""
            <p class="info">{ip}</p>
            <p class="info">{country}{city}</p>
            <p class="info"{lng:.5f}:{lat:.5f}</p>
        """
        )
#    @staticmethod
#    def userAccount(request):
#        userAccount=''
#        if "userAccount" in request.session:
#            userAccount=request.session["userAccount"]
#        return userAccount
